from typing import Dict

from src.behavioral.command.core.notifier import Notifier
from src.behavioral.command.domain.email.email_sender import EmailSender


class EmailNotifier(Notifier):

    def __init__(self, data: Dict[str, str]):
        self.sender = EmailSender()
        self.data = data

    def notify(self):
        self.sender.send(self.data)
