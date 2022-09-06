from src.creational.builder.domain.drink.drink import Drink


class Sprite(Drink):

    def __init__(self):
        super().__init__("Sprite", 2.65)

