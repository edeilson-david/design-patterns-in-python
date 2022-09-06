from src.creational.abstract_factory.core.drive import Drive


class OneDrive(Drive):

    def upload(self, file: str) -> None:
        print(f"Uploading file to OneDrive: {file}")
