from typing import Dict

from src.behavioral.command.core.sender import Sender


class EmailSender(Sender):

    def send(self, data: Dict[str, str]):
        print(f"Send Email: {data['subject']}")
