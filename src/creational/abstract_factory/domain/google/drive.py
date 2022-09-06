from src.creational.abstract_factory.core.drive import Drive


class GoogleDrive(Drive):

    def upload(self, file: str) -> None:
        print(f"Uploading file to Google Drive: {file}")
