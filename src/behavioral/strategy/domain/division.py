from src.behavioral.strategy.core.math_operation import MathOperation


class Division(MathOperation):

    def calc(self, first: float, second: float):
        result = first / second
        print(f"Division result is: {result}")
