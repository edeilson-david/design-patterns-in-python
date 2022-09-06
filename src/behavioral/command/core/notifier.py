import abc


class Notifier(abc.ABC):

    @abc.abstractmethod
    def notify(self):
        pass
