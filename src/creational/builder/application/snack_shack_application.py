from src.commons.app_runner import AppRunner
from src.creational.builder.core.default_order_printer import DefaultOrderPrinter
from src.creational.builder.core.order_builder import OrderBuilder
from src.creational.builder.domain.burger.beef_burger import BeefBurger
from src.creational.builder.domain.burger.chicken_burger import ChickenBurger
from src.creational.builder.domain.drink.coke import Coke
from src.creational.builder.domain.drink.pepsi import Pepsi
from src.creational.builder.domain.drink.sprite import Sprite
from src.creational.builder.domain.drink.tea import Tea
from src.creational.builder.domain.fries.crinkle_fries import CrinkleFries


class SnackShackBurgersApplication(AppRunner):

    def execute(self, args: list):
        order_printer = DefaultOrderPrinter()

        order_001 = (OrderBuilder()
                     .with_burger(BeefBurger(), {"Pickles"})
                     .with_fries(CrinkleFries(), {"Bacon"})
                     .with_drink(Coke(), {'without ice'})
                     .build())
        order_printer.print(order_001)

        order_002 = (OrderBuilder()
                     .with_fries(CrinkleFries(), {"Cheddar", "Bacon"})
                     .with_drink(Pepsi())
                     .build())
        order_printer.print(order_002)

        order_003 = (OrderBuilder()
                     .with_burger(ChickenBurger())
                     .with_drink(Tea(), {'without ice'})
                     .build())
        order_printer.print(order_003)

        order_004 = (OrderBuilder()
                     .with_drink(Sprite())
                     .build())
        order_printer.print(order_004)


if __name__ == "__main__":
    AppRunner.run(SnackShackBurgersApplication, [])
