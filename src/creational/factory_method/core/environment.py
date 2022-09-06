from enum import Enum

from src.creational.factory_method.core.environment_exception import EnvironmentException


class Environment(Enum):
    WINDOWS = "windows"
    MAC = "mac"

    @staticmethod
    def get(name: str):
        try:
            return Environment[name.upper()]
        except KeyError:
            message = f'The parameter is not accepted. Consider one of these: {[value.name for value in Environment]}'
            raise EnvironmentException(message) from None
