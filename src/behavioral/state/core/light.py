from __future__ import annotations

from abc import ABC, abstractmethod


class Light(ABC):

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def next(self) -> Light:
        pass
