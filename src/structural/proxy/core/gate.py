import abc


class Gate(abc.ABC):

    @abc.abstractmethod
    def open(self, credential: str):
        pass

    @abc.abstractmethod
    def close(self):
        pass
