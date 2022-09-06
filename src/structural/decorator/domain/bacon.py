from src.structural.decorator.core.pastry import Pastry
from src.structural.decorator.domain.additional_items import AdditionalPastryItem


class Bacon(AdditionalPastryItem):

    def __init__(self, item: Pastry):
        super().__init__(item)

    def get_ingredients(self) -> str:
        return self.item.get_ingredients() + ", bacon"

    def get_cost(self) -> float:
        return self.item.get_cost() + 0.98
