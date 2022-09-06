from src.creational.builder.domain.drink.drink import Drink


class Pepsi(Drink):

    def __init__(self):
        super().__init__("Pepsi", 2.80)
