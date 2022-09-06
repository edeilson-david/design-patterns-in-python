from __future__ import annotations
from src.structural.decorator.core.pastry import Pastry


class AdditionalPastryItem(Pastry):

    def __init__(self, item: Pastry):
        self.item = item

    def get_ingredients(self) -> str:
        return self.item.get_ingredients()

    def get_cost(self) -> float:
        return self.item.get_cost()
