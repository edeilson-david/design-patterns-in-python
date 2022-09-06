import abc

from src.behavioral.mediator.domain.user import User


class Room(abc.ABC):

    @abc.abstractmethod
    def show_message(self, user: User, user_receive: User, message: str):
        pass

