from typing import Dict

from src.behavioral.command.core.sender import Sender


class SMSSender(Sender):

    def send(self, data: Dict[str, str]):
        print(f"Send SMS: {data['subject']}")
