import abc


class Cashier(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def calculate(self, ticket):
        pass
