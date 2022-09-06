from __future__ import annotations

import abc
from typing import Set

from src.creational.builder.core.order import Order
from src.creational.builder.domain.burger.burger import Burger
from src.creational.builder.domain.drink.drink import Drink
from src.creational.builder.domain.fries.fries import Fries


class OrderBuilder(abc.ABC):

    def __init__(self):
        self._order = Order()

    def with_burger(self, burger: Burger, additional_items: Set[str] = {}) -> OrderBuilder:
        self._order.with_burger(burger, additional_items)
        return self

    def with_fries(self, fries: Fries, additional_items: Set[str] = {}) -> OrderBuilder:
        self._order.with_fries(fries, additional_items)
        return self

    def with_drink(self, drink: Drink, notes: Set[str] = {}) -> OrderBuilder:
        self._order.with_drink(drink, notes)
        return self

    def build(self) -> Order:
        return self._order
