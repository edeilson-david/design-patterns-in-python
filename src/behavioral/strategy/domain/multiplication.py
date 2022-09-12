from src.behavioral.strategy.core.math_operation import MathOperation


class Multiplication(MathOperation):

    def calc(self, first: float, second: float):
        result = first * second
        print(f"Multiplication result is: {result}")
