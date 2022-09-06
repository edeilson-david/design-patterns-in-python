from __future__ import annotations

import abc


class MenuComponent(abc.ABC):

    def __init__(self, label: str):
        self._index = 0
        self._label = label

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index: int):
        self._index = index

    def append(self, item: MenuComponent) -> MenuComponent:
        return self

    def remove(self, item: MenuComponent) -> MenuComponent:
        return self

    def render(self):
        TAB = "\t" * self._index
        print(f"{TAB}{self._label}")
