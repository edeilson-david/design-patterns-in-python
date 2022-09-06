from typing import Dict

from src.behavioral.command.core.notifier import Notifier
from src.behavioral.command.domain.slack.slack_sender import SlackSender


class SlackNotifier(Notifier):

    def __init__(self, data: Dict[str, str]):
        self.sender = SlackSender()
        self.data = data

    def notify(self):
        self.sender.send(self.data)

