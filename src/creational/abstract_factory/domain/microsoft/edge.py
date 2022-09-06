from src.creational.abstract_factory.core.browser import Browser


class MicrosoftEdge(Browser):

    def access_website(self, url: str) -> None:
        print(f"Accessing page from Microsoft Edge: {url}")
