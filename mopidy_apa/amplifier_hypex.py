from gpiozero import OutputDevice

from mopidy_apa.amplifier_base import AmplifierBase


class AmplifierHypex(AmplifierBase):
    """Class to provide amplifier control services for Hypex from a Raspberry PI."""

    def __init__(self) -> None:
        self.smps_standby = OutputDevice(24)
        self.amplifier_standby = OutputDevice(23)

    @property
    def psu_on(self) -> bool:
        # SMPS is on if voltage is low
        return self.smps_standby.value == 0

    @psu_on.setter
    def psu_on(self, newvalue: bool) -> None:
        if newvalue:
            # i.e. set on by pulling voltage to low
            self.smps_standby.off()
        else:
            # i.e. set off by pulling voltage to high
            self.smps_standby.on()

    @property
    def amp_on(self) -> bool:
        # amplifier is on if voltage is low
        return self.smps_standby.value == 0

    @amp_on.setter
    def amp_on(self, newvalue: bool) -> None:
        if newvalue:
            # i.e. set on by pulling voltage to low
            self.amplifier_standby.off()
        else:
            # i.e. set off by pulling voltage to high
            self.amplifier_standby.on()
