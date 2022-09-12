from src.behavioral.strategy.core.math_operation import MathOperation


class Subtraction(MathOperation):

    def calc(self, first: float, second: float):
        result = first - second
        print(f"Subtraction result is: {result}")
