from src.creational.builder.domain.burger.burger import Burger


class ChickenBurger(Burger):

    def __init__(self):
        super().__init__("Chicken Burger", 4.56)

