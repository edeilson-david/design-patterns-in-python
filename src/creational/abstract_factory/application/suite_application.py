from src.commons.app_runner import AppRunner
from src.creational.abstract_factory.core.suite import Suite
from src.creational.abstract_factory.core.suite_factory import SuiteFactory
from src.creational.abstract_factory.domain.google.google_suite_factory import GoogleSuiteFactory
from src.creational.abstract_factory.domain.microsoft.microsoft_suite_factory import MicrosoftSuiteFactory


class SuiteApplication(AppRunner):

    def execute(self, args: list):
        suite = Suite.get(args[0])
        suite_factory = SuiteApplication._create_suite_factory(suite)

        # Searching new travel opportunity...
        browser = suite_factory.get_browser()
        browser.access_website("www.travelforyou.com")

        # Contacting the hotel to booking...
        mail = suite_factory.get_email()
        subject = "Booking"
        content = "Hello!" \
                  "\n\tI would like a reservation for " \
                  "\n\ttwo adults and one child on the 4th."
        mail.send(subject, content)

        # Emptying memory card. Making backups on cloud drive...
        drive = suite_factory.get_drive()
        drive.upload("last_travel_photos_beach.zip")

    @staticmethod
    def _create_suite_factory(suite: Suite) -> SuiteFactory:
        if suite is Suite.WINDOWS:
            return MicrosoftSuiteFactory()

        if suite is Suite.GOOGLE:
            return GoogleSuiteFactory()


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if 0 == len(args):
        args = ["google"]
    AppRunner.run(SuiteApplication, args)
