from src.behavioral.state.core.light import Light
from src.behavioral.state.domain.green_light import GreenLight


class Semaphore:

    def __init__(self) -> None:
        self._current = GreenLight()

    def change(self, light: Light):
        self._current = light
        self._current.context = self

    def display(self):
        self._current.action()
        self._current = self._current.next()
