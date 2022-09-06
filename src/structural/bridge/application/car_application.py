from src.commons.app_runner import AppRunner
from src.structural.bridge.domain.car.sportcar import SportCar
from src.structural.bridge.domain.color.red import Red


class CarApplication(AppRunner):

    def execute(self, args: list):

        red = Red()
        car = SportCar("Ferrari", 2, red)
        car.info()


if __name__ == "__main__":
    AppRunner.run(CarApplication, [])
