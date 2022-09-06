from datetime import datetime

from src.creational.singleton.core.singleton import SingletonThread
from src.creational.singleton.domain.logger.loggable import Loggable


class ElasticsearchLogger(Loggable, metaclass=SingletonThread):

    def __init__(self, logger_name: str):
        super().__init__(logger_name)

    def log(self, message: str):
        print(f"{datetime.utcnow()} [{self.logger_name}] {message}")
