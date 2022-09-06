from src.creational.abstract_factory.core.browser import Browser
from src.creational.abstract_factory.core.drive import Drive
from src.creational.abstract_factory.core.email import Email
from src.creational.abstract_factory.core.suite_factory import SuiteFactory
from src.creational.abstract_factory.domain.microsoft.edge import MicrosoftEdge
from src.creational.abstract_factory.domain.microsoft.one_drive import OneDrive
from src.creational.abstract_factory.domain.microsoft.outlook import Outlook


class MicrosoftSuiteFactory(SuiteFactory):

    def get_browser(self) -> Browser:
        return MicrosoftEdge()

    def get_drive(self) -> Drive:
        return OneDrive()

    def get_email(self) -> Email:
        return Outlook()
