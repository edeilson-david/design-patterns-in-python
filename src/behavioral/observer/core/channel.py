from abc import ABC, abstractmethod

from src.behavioral.observer.core.subscriber import Subscriber
from src.behavioral.observer.domain.video import Video


class Channel(ABC):

    @abstractmethod
    def upload(self, video: Video):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def subscribe(self, user: Subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, user: Subscriber):
        pass
