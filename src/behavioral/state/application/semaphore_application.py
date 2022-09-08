from src.behavioral.state.domain.semaphore import Semaphore
from src.commons.app_runner import AppRunner


class SemaphoreApplication(AppRunner):

    def execute(self, args: list):
        semaphore = Semaphore()
        semaphore.display()
        semaphore.display()
        semaphore.display()


if __name__ == "__main__":
    AppRunner.run(SemaphoreApplication, [])
