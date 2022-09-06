import abc


class Browser(abc.ABC):

    @abc.abstractmethod
    def access_website(self, url: str) -> None:
        pass
