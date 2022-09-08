from src.behavioral.observer.core.subscriber import Subscriber
from src.behavioral.observer.domain.video import Video


class User(Subscriber):

    def __init__(self, username: str):
        self.username = username

    def update(self, video: Video):
        print(f"Hello {self.username}! We have a new video. Go to out channel and watch the '{video.filename}' video.")
