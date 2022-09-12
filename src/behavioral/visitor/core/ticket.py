import abc


class Ticket(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def price(self) -> float:
        pass

    @abc.abstractmethod
    def accept(self, cashier):
        pass
