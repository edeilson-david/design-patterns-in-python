import abc


class Drive(abc.ABC):

    @abc.abstractmethod
    def upload(self, file: str) -> None:
        pass
