from src.behavioral.template_method.core.file_reader import FileReader


class PDFReader(FileReader):

    def _open(self):
        print("[PDF Reader] - Opening file...")

    def _read(self):
        print("[PDF Reader] - Reading file...")

    def _close(self):
        print("[PDF Reader] - Closing file...")
