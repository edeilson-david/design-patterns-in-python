from src.behavioral.memento.domain.document import Document
from src.behavioral.memento.domain.editor import Editor
from src.commons.app_runner import AppRunner


class QueueManagerApplication(AppRunner):

    def execute(self, args: list):

        document = Document("customer_data.txt")
        editor = Editor(document)
        editor.write("Header")
        editor.write("Paragraph 1")
        editor.write("Text 1")
        editor.save()

        editor.write("Text 2")
        editor.save()
        editor.undo()

        editor.write("Paragraph 1")
        editor.write("Text 2")
        editor.save()


if __name__ == "__main__":
    AppRunner.run(QueueManagerApplication, [])
