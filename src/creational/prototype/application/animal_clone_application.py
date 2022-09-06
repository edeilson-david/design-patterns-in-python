from src.commons.app_runner import AppRunner
from src.creational.prototype.domain.sheep import Sheep


class AnimalCloneApplication(AppRunner):

    def execute(self, args: list):
        dolly = Sheep()

        sheep_cloned = dolly.clone()
        fake_cloned = dolly

        AnimalCloneApplication.check_is_the_same(dolly, sheep_cloned)
        AnimalCloneApplication.check_is_the_same(dolly, fake_cloned)

        # Why? Because hash values are different.
        print(f"")
        AnimalCloneApplication.print_hash_value(dolly)
        AnimalCloneApplication.print_hash_value(sheep_cloned)
        AnimalCloneApplication.print_hash_value(fake_cloned)

    @staticmethod
    def check_is_the_same(st_sheed: Sheep, nd_sheep: Sheep):
        print(f"Is the same sheep? {'Yes' if st_sheed == nd_sheep else 'No'}")

    @staticmethod
    def print_hash_value(sheep: Sheep):
        print(f"Hash value of the instance: {sheep.__hash__()}")


if __name__ == "__main__":
    AppRunner.run(AnimalCloneApplication, [])
