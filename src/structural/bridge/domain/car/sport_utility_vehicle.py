from src.structural.bridge.core.car import Car
from src.structural.bridge.core.color import Color


class SUV(Car):

    def __init__(self, name: str, seats: int, color: Color):
        super().__init__("SUV", name, seats, color)
