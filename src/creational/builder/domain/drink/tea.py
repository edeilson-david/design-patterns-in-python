from src.creational.builder.domain.drink.drink import Drink


class Tea(Drink):

    def __init__(self):
        super().__init__("Cold Tea", 1.64)

