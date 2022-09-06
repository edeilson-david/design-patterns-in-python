from src.behavioral.mediator.core.room import Room
from src.behavioral.mediator.domain.user import User


class ChatRoom(Room):

    def __init__(self):
        self._users = list()

    def enter(self, user: User) -> None:
        self._users.append(user)

    def show_message(self, sender: User, receiver: User, message: str) -> None:
        print(f"[{str(receiver.username + ' screen').upper()}]: {sender.username} said: '{message}'")

    def send_message(self, sender: User, message: str) -> None:
        for receiver in self._users:
            if receiver != sender:
                self.show_message(sender, receiver, message)
            continue

        print("-" * 50)
