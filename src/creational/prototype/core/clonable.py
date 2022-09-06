from __future__ import annotations
import abc
import copy


class Clonable(abc.ABC):

    def clone(self) -> Clonable:
        return copy.copy(self)
