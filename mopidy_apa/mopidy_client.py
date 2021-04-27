import copy
import logging
import queue

import pykka
from mopidy import core

from mopidy_apa.amplifier_controller import AmplifierController, PlayerState
from mopidy_apa.amplifier_hypex import AmplifierHypex

log = logging.getLogger(__name__)


class MopidyClient(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super().__init__()
        self.core = core
        self.confg = config
        self.status_queue = None

    def on_start(self):
        log.info("MopidyClient start")
        self.player_state = PlayerState.Idle
        self.status_queue = queue.Queue()

        amp_delay = self.config.get("amp_delay", 60)
        psu_delay = self.config.get("psu_delay", 300)
        amplifier = AmplifierHypex()
        self.controller = AmplifierController(
            self.status_queue,
            amplifier,
            amp_delay,
            psu_delay,
            self.player_state,
        )
        self.controller.start()

    def on_stop(self):
        log.info("MopidyClient stop")
        self.controller.stop()
        self.controller = None
        self.status_queue.join()

    def seeked(self, time_position):
        self.player_state = PlayerState.Active
        self._queue_status()

    def stream_title_changed(self, title):
        self.player_state = PlayerState.Active
        self._queue_status()

    def track_playback_ended(self, tl_track, time_position):
        self.player_state = PlayerState.Idle
        self._queue_status()

    def track_playback_paused(self, tl_track, time_position):
        self.player_state = PlayerState.Idle
        self._queue_status()

    def track_playback_resumed(self, tl_track, time_position):
        self.player_state = PlayerState.Active
        self._queue_status()

    def track_playback_started(self, tl_track):
        self.player_state = PlayerState.Active
        self._queue_status()

    def volume_changed(self, volume):
        self.player_state = PlayerState.Active
        self._queue_status()

    def _queue_status(self):
        new_status = copy.copy(self.player_state)
        self.status_queue.put(new_status, block=False)
