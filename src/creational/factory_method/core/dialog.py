from __future__ import annotations
from abc import ABC, abstractmethod

from src.creational.factory_method.core.button import Button


class Dialog(ABC):

    @abstractmethod
    def createButton(self) -> Button:
        pass
