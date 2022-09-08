from typing import List

from src.behavioral.observer.core.channel import Channel
from src.behavioral.observer.core.subscriber import Subscriber
from src.behavioral.observer.domain.video import Video


class BlogChannel(Channel):
    _subscribers: List[Subscriber] = []

    def __init__(self):
        self.video = None
        self.subscribers = []

    def subscribe(self, user: Subscriber):
        self._subscribers.append(user)

    def unsubscribe(self, user: Subscriber):
        self._subscribers.remove(user)

    def upload(self, video: Video):
        self.video = video
        self.notify()

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self.video)
