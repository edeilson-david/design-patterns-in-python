from typing import Dict

from src.behavioral.command.core.sender import Sender


class SlackSender(Sender):

    def send(self, data: Dict[str, str]):
        print(f"Send Slack: {data['subject']}")
