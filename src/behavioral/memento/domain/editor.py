import datetime

from src.behavioral.memento.domain.document import Document
from src.behavioral.memento.domain.status import Status


class Editor:

    def __init__(self, document: Document):
        self.document = document
        self.history = list()

    def write(self, content: str):
        self.document.write(content)

    def save(self):
        if 3 == len(self.history):
            status = self.history[0]
            self.history.remove(status)

        self.document.date = datetime.datetime.now()
        status = Status(self.document)
        self.history.append(status)

        print(f"File saved at: {self.document.date}")
        print(f"Content file: {self.document.content}")
        print("")

    def undo(self):
        if 0 == len(self.history):
            return

        if 1 == len(self.history):
            print("Last history saved: ")
            self.document = self.history[len(self.history) - 1].document

        else:
            index = len(self.history) - 1

            last_document = self.history[index]
            self.history.remove(last_document)

            self.document = self.history[len(self.history) - 1].document

        print(f"Date restore to: {self.document.date}")
        print(f"Content file: {self.document.content}")
        print("")
