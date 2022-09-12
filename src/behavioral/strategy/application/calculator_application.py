from src.behavioral.strategy.core.calculator import Calculator
from src.behavioral.strategy.domain.subtraction import Subtraction
from src.commons.app_runner import AppRunner


class CalculatorApplication(AppRunner):

    def execute(self, args: list):
        # Default strategy is Additional
        calculator = Calculator()
        calculator.calc(1, 2)
        calculator.calc(6, 2)

        # Change the strategy
        calculator.set_operation(Subtraction())
        calculator.calc(5, 3)
        calculator.calc(9, 6)


if __name__ == "__main__":
    AppRunner.run(CalculatorApplication, [])
