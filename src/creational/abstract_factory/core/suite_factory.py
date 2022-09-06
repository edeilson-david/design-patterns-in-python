import abc

from src.creational.abstract_factory.core.browser import Browser
from src.creational.abstract_factory.core.drive import Drive
from src.creational.abstract_factory.core.email import Email


class SuiteFactory(abc.ABC):

    @abc.abstractmethod
    def get_browser(self) -> Browser:
        pass

    @abc.abstractmethod
    def get_drive(self) -> Drive:
        pass

    @abc.abstractmethod
    def get_email(self) -> Email:
        pass
