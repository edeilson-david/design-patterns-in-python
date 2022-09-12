from src.behavioral.strategy.core.math_operation import MathOperation
from src.behavioral.strategy.domain.addition import Addition


class Calculator:

    def __init__(self):
        self._operation = Addition()

    def set_operation(self, operation: MathOperation):
        self._operation = operation

    def calc(self, first: float, second: float):
        self._operation.calc(first, second)
