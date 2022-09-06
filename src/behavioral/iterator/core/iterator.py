import abc

from src.behavioral.iterator.domain.customer import Customer


class Iterator(abc.ABC):

    @abc.abstractmethod
    def has_next(self) -> bool:
        pass

    @abc.abstractmethod
    def get(self) -> Customer:
        pass
