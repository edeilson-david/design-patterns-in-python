from copy import copy

from src.behavioral.memento.domain.document import Document


class Status:

    def __init__(self, document: Document):
        self.document = Document(document.filename)
        self.document.content = copy(document.content)
        self.document.date = copy(document.date)
