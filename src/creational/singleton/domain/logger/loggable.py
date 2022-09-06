from abc import abstractmethod


class Loggable:

    def __init__(self, logger_name: str):
        self._logger_name = logger_name
        print(f"Instantiate: {logger_name}")

    @property
    def logger_name(self):
        return self._logger_name

    @abstractmethod
    def log(self, message: str):
        pass
