from enum import Enum

from src.creational.factory_method.core.environment_exception import EnvironmentException


class Suite(Enum):
    WINDOWS = "windows"
    GOOGLE = "google"

    @staticmethod
    def get(name: str):
        try:
            return Suite[name.upper()]
        except KeyError:
            message = f'The parameter is not accepted. Consider one of these: {[value.name for value in Suite]}'
            raise EnvironmentException(message) from None
