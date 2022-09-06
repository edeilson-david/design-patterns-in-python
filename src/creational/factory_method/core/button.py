from __future__ import annotations
from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def on_click(self) -> None:
        pass
