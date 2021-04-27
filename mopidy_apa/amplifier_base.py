import abc


class AmplifierBase(metaclass=abc.ABCMeta):
    """Abstract base class to provide amplifier control services."""

    @property
    @abc.abstractmethod
    def amp_on(self) -> bool:
        pass

    @amp_on.setter
    def amp_on(self, newvalue: bool) -> None:
        return

    @property
    @abc.abstractmethod
    def psu_on(self) -> bool:
        pass

    @psu_on.setter
    def psu_on(self, newvalue: bool) -> None:
        return
