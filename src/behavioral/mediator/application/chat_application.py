from src.behavioral.mediator.domain.chatroom import ChatRoom
from src.behavioral.mediator.domain.user import User
from src.commons.app_runner import AppRunner


class QueueManagerApplication(AppRunner):

    def execute(self, args: list):
        kelly = User("Kelly")
        eddie = User("Eddie")
        jane = User("Jane")

        room = ChatRoom()
        room.enter(kelly)
        room.enter(eddie)
        room.enter(jane)

        room.send_message(kelly, "Hi everone!")
        room.send_message(eddie, "Hi!")
        room.send_message(jane, "Hello!")


if __name__ == "__main__":
    AppRunner.run(QueueManagerApplication, [])
