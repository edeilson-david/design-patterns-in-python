from abc import ABC, abstractmethod


class AppRunner(ABC):

    @abstractmethod
    def execute(self, args: list):
        pass

    @staticmethod
    def run(filename, args: list):
        import importlib
        module = importlib.import_module(filename.__module__)
        clazz = getattr(module, filename.__name__)
        instance = clazz()
        instance.execute(args)
