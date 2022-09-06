import abc

from src.structural.bridge.core.color import Color


class Car(abc.ABC):

    def __init__(self, model: str, name: str, seats: int, color: Color):
        self._model = model
        self._name = name
        self._seats = seats
        self._color = color

    def info(self) -> None:
        print(f"Characteristics car")
        print(f"Model: {self._model}")
        print(f"Color: {self._color.name}")
        print(f"Name: {self._name}")
        print(f"Seats: {self._seats}")
