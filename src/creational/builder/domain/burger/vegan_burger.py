from src.creational.builder.domain.burger.burger import Burger


class VeganBurger(Burger):

    def __init__(self):
        super().__init__("Vegan Burger", 4.15)

