import abc


class Sender(abc.ABC):

    @abc.abstractmethod
    def send(self, data: str):
        pass
