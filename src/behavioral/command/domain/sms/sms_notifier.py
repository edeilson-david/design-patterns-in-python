from typing import Dict

from src.behavioral.command.core.notifier import Notifier
from src.behavioral.command.domain.sms.sms_sender import SMSSender


class SMSNotifier(Notifier):

    def __init__(self, data: Dict[str, str]):
        self.sender = SMSSender()
        self.data = data

    def notify(self):
        self.sender.send(self.data)

