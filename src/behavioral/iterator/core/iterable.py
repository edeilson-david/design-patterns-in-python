import abc

from src.behavioral.iterator.domain.customer import Customer


class Iterable(abc.ABC):

    @abc.abstractmethod
    def add(self, customer: Customer) -> None:
        pass
