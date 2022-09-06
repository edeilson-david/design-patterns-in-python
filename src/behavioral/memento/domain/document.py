from datetime import datetime


class Document:

    def __init__(self, filename: str):
        self.filename = filename
        self.content = list()
        self.date = str(datetime.now())

    def write(self, content: str):
        self.content.append(content)
