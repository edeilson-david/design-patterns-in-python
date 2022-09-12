from src.behavioral.strategy.core.math_operation import MathOperation


class Addition(MathOperation):

    def calc(self, first: float, second: float):
        result = first + second
        print(f"Additional result is: {result}")
