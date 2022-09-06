from src.creational.abstract_factory.core.email import Email


class Outlook(Email):

    def send(self, subject: str, content: str) -> None:
        print(f"Sending email from Outlook."
              f"\nSubject: {subject}"
              f"\nContent: {content}")
