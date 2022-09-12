from src.behavioral.template_method.domain.pdf_reader import PDFReader
from src.commons.app_runner import AppRunner


class FileReaderApplication(AppRunner):

    def execute(self, args: list):
        reader = PDFReader()
        reader.extract()


if __name__ == "__main__":
    AppRunner.run(FileReaderApplication, [])
