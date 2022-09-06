from __future__ import annotations


class Customer:

    def __hash__(self):
        return hash((self._name, self._passwd))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._passwd == other._passwd and self._name == other._name

    def __init__(self, name: str, passwd: str) -> None:
        self._name: str = name
        self._passwd: str = passwd

    @property
    def name(self) -> str:
        return self._name

    @property
    def passwd(self) -> str:
        return self._passwd
