from src.behavioral.template_method.core.file_reader import FileReader


class TextReader(FileReader):

    def _open(self):
        print("[Text Reader] - Opening file...")

    def _read(self):
        print("[Text Reader] - Reading file...")

    def _close(self):
        print("[Text Reader] - Closing file...")
