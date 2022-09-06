from datetime import datetime

from src.creational.singleton.core.singleton_threads import SingletonMultiThread
from src.creational.singleton.domain.logger.loggable import Loggable


class ConsoleLoggerThreads(Loggable, metaclass=SingletonMultiThread):

    def __init__(self, logger_name: str):
        super().__init__(logger_name)

    def log(self, message: str):
        print(f"{datetime.utcnow()} [{self.logger_name}] {message}\n")
