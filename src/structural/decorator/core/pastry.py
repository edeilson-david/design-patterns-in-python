from __future__ import annotations

import abc


class Pastry(abc.ABC):

    @abc.abstractmethod
    def get_ingredients(self) -> str:
        pass

    @abc.abstractmethod
    def get_cost(self) -> float:
        pass

    def get_tax(self) -> float:
        return self.get_cost() * 0.1
