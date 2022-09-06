from src.behavioral.command.core.notifier import Notifier


class Executor:

    def __init__(self):
        self.history = []

    def execute(self, command: Notifier):
        self.history.append(command)
        command.notify()
