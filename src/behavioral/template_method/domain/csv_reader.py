from src.behavioral.template_method.core.file_reader import FileReader


class CSVReader(FileReader):

    def _open(self):
        print("[CSV Reader] - Opening file...")

    def _read(self):
        print("[CSV Reader] - Reading file...")

    def _close(self):
        print("[CSV Reader] - Closing file...")
