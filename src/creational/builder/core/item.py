from __future__ import annotations

from abc import ABC


class Item(ABC):

    def __hash__(self):
        return hash((self._name, self._cost))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._name == other._name and self._cost == other._cost

    def __init__(self, name: str, cost: float) -> None:
        self._additional_notes = set()
        self._additional_items = set()
        self._name: str = name
        self._cost: float = cost

    def add_items(self, item_name: str) -> Item:
        additional_item = Item(item_name, 2.5)
        self._additional_items.add(additional_item)
        self._update_cost(additional_item._cost)
        return self

    def add_notes(self, note: str) -> Item:
        self._additional_notes.add(note)
        return self

    def _update_cost(self, cost: float):
        self._cost += cost

    @property
    def name(self) -> str:
        return self._name

    @property
    def cost(self) -> float:
        return self._cost

    @property
    def additional_items(self):
        return self._additional_items

    @property
    def additional_notes(self):
        return self._additional_notes
