import abc


class MathOperation(abc.ABC):

    @abc.abstractmethod
    def calc(self, first: float, second: float):
        pass
