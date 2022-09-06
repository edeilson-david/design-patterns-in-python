import abc


class MemoryCard(abc.ABC):

    def __init__(self, name: str, pins: int):
        self._name = name
        self._pins = pins

    @property
    def name(self) -> str:
        return self._name

    @property
    def pins(self) -> int:
        return self._pins
