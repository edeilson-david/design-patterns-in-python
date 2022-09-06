from src.creational.builder.domain.burger.burger import Burger


class BeefBurger(Burger):

    def __init__(self):
        super().__init__("Beef Burger", 5.09)

