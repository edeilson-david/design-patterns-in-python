from abc import ABC, abstractmethod

from src.behavioral.observer.domain.video import Video


class Subscriber(ABC):

    @abstractmethod
    def update(self, video: Video) -> None:
        pass
