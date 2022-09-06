from src.structural.bridge.core.car import Car
from src.structural.bridge.core.color import Color


class Hatchback(Car):

    def __init__(self, name: str, seats: int, color: Color):
        super().__init__("Hatchback", name, seats, color)
