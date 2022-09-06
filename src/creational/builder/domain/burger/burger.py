from abc import ABC

from src.creational.builder.core.item import Item


class Burger(Item, ABC):

    def __init__(self, name: str, cost: float):
        super().__init__(name, cost)
