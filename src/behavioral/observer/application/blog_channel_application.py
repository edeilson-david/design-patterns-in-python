from src.behavioral.observer.domain.blog_channel import BlogChannel
from src.behavioral.observer.domain.user import User
from src.behavioral.observer.domain.video import Video
from src.commons.app_runner import AppRunner


class BlogChannelApplication(AppRunner):

    def execute(self, args: list):
        channel = BlogChannel()

        mary = User("Mary")
        channel.subscribe(mary)

        joseph = User("Joseph")
        channel.subscribe(joseph)

        video = Video("Funny squirrel")
        channel.upload(video)


if __name__ == "__main__":
    AppRunner.run(BlogChannelApplication, [])
