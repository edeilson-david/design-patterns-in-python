from __future__ import annotations
from src.structural.decorator.core.pastry import Pastry


class MiniCheesePastry(Pastry):

    def get_ingredients(self) -> str:
        return "cheese"

    def get_cost(self) -> float:
        return 2.38
