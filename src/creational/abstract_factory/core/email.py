import abc


class Email(abc.ABC):

    @abc.abstractmethod
    def send(self, subject: str, content: str) -> None:
        pass
