from typing import Set

from src.creational.builder.core.item import Item
from src.creational.builder.domain.burger.burger import Burger
from src.creational.builder.domain.drink.drink import Drink
from src.creational.builder.domain.fries.fries import Fries


class Order:

    def __init__(self):
        self._burger: Burger = Item
        self._fries: Fries = Item
        self._drink: Drink = Item
        self._total_cost = 0

    def with_burger(self, burger: Burger, additional_items: Set[str] = {}):
        self._burger = burger

        if 3 < len(additional_items):
            raise Exception("It is only allow 3 additional items.")

        for additonal in additional_items:
            self._burger.add_items(additonal)
        self._total_cost += self._burger.cost

    def with_fries(self, fries: Fries, additional_items: Set[str] = {}):
        self._fries = fries

        if 3 < len(additional_items):
            raise Exception("It is only allow 3 additional items.")

        for additonal in additional_items:
            self._fries.add_items(additonal)
        self._total_cost += self._fries.cost

    def with_drink(self, drink: Drink, notes: Set[str] = {}):
        self._drink = drink
        for note in notes:
            self._drink.add_notes(note)
        self._total_cost += self._drink.cost

    @property
    def burger(self):
        return self._burger

    @property
    def fries(self):
        return self._fries

    @property
    def drink(self):
        return self._drink

    @property
    def total_cost(self):
        return self._total_cost
