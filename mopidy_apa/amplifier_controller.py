import logging
import queue
import threading
import time
from datetime import datetime
from enum import Enum
from typing import Optional

log = logging.getLogger(__name__)


class PlayerState(Enum):
    Idle = 0
    Active = 1


class AmplifierController(object):
    last_state: PlayerState
    last_update: datetime
    switchoff_delay: float

    def __init__(
        self,
        status_queue,
        amplifier,
        amp_delay: float,
        psu_delay: float,
        state: PlayerState,
    ) -> None:
        self.status_queue = status_queue
        self.amplifier = amplifier
        self.amp_delay = amp_delay
        self.psu_delay = psu_delay
        self.last_state = state
        self.last_update = datetime.now()
        self._delay = 0.5
        self._thread = None

    def start(self):
        log.info("Amplifier update loop starting ...")
        if self._thread is not None:
            return

        self._running = threading.Event()
        self._running.set()
        self._thread = threading.Thread(target=self._loop)
        self._thread.start()

    def stop(self):
        self._running.clear()
        self._thread.join()
        self._thread = None

    def _loop(self):
        log.info("Amplifier update loop started")
        while self._running.is_set():
            player_state = None
            try:
                player_state = self.status_queue.get(timeout=self._delay)
                self.status_queue.task_done()

            except queue.Empty:
                pass
            finally:
                self._update(player_state)

            time.sleep(self._delay)
        log.info("Amplifier update loop stopped")

    def _update(self, new_status: Optional[PlayerState]) -> None:
        """Update amplifier with latest player state."""

        timestamp = datetime.now()

        if new_status is None:
            if self.last_state == PlayerState.Idle:
                delta = timestamp - self.last_update
                if (
                    self.amplifier.amp_on
                    and delta.total_seconds() > self.amp_delay
                ):
                    log.info("Power off audio amplifier")
                    self.amplifier.amp_on = False
                if (
                    self.amplifier.psu_on
                    and delta.total_seconds() > self.psu_delay
                ):
                    log.info("Power off power supplu")
                    self.amplifier.psu_on = False
        else:
            if not self.amplifier.psu_on:
                log.info("Power on power supply")
                self.amplifier.psu_on = True
                time.sleep(self._delay)

            if not self.amplifier.amp_on:
                log.info("Power on audio amplifier")
                self.amplifier.amp_on = True

            self.last_state = new_status

        self.last_update = timestamp
