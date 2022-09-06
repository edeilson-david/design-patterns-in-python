from __future__ import annotations
from src.structural.composite.core.menu_component import MenuComponent
from src.structural.composite.domain.item import Item


class SubItem(MenuComponent):

    def __init__(self, label: str, index: int = 0):
        super().__init__(label)
        self.index = index
        self._items = []

    def append(self, item: Item) -> SubItem:
        item.index = self.index + 1
        self._items.append(item)
        return self

    def remove(self, item: Item) -> SubItem:
        self._items.remove(item)
        return self

    def render(self):
        super().render()

        items = self._items
        if 0 < len(items):
            for item in items:
                item.render()
