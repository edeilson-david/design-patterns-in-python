from src.creational.builder.core.item import Item
from src.creational.builder.domain.drink.drink import Drink


class Coke(Drink):

    def __init__(self):
        super().__init__("Coke", 2.80)

    def add_items(self, item_name: str) -> Item:
        print("Is not possible add an item to Coke Drink.")
