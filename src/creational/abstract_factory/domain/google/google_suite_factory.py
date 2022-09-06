from src.creational.abstract_factory.core.browser import Browser
from src.creational.abstract_factory.core.drive import Drive
from src.creational.abstract_factory.core.email import Email
from src.creational.abstract_factory.core.suite_factory import SuiteFactory
from src.creational.abstract_factory.domain.google.chrome import GoogleChrome
from src.creational.abstract_factory.domain.google.drive import GoogleDrive
from src.creational.abstract_factory.domain.google.gmail import Gmail


class GoogleSuiteFactory(SuiteFactory):

    def get_browser(self) -> Browser:
        return GoogleChrome()

    def get_drive(self) -> Drive:
        return GoogleDrive()

    def get_email(self) -> Email:
        return Gmail()
