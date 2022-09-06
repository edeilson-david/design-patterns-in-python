from src.creational.abstract_factory.core.email import Email


class Gmail(Email):

    def send(self, subject: str, content: str) -> None:
        print(f"Sending email from Gmail."
              f"\nSubject: {subject}"
              f"\nContent: {content}")
