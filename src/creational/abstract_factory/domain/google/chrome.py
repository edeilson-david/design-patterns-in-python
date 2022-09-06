from src.creational.abstract_factory.core.browser import Browser


class GoogleChrome(Browser):

    def access_website(self, url: str) -> None:
        print(f"Accessing page from Google Chrome: {url}")
