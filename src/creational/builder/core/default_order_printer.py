from src.creational.builder.core.item import Item
from src.creational.builder.core.order import Order
from src.creational.builder.domain.burger.burger import Burger
from src.creational.builder.domain.drink.drink import Drink
from src.creational.builder.domain.fries.fries import Fries


class DefaultOrderPrinter:

    def __init__(self):
        self._colsize = 80

    def print(self, order: Order):
        print(f"".ljust(self._colsize, '-'))
        print(f"SnackShack Burgers®".rjust(50, ' '))
        print(f"".ljust(self._colsize, '-'))
        self._print_info(order.burger, Burger)
        self._print_info(order.fries, Fries)
        self._print_info(order.drink, Drink)
        print(f"Total: {round(order.total_cost, 2)}".rjust(80, ' '))
        print(f"".ljust(self._colsize, '-'))

    def _print_info(self, item: Item, item_type):
        if not isinstance(item, item_type):
            return

        print(f'Item description: {item.name}'.ljust(50) + f' Cost: {item.cost}'.rjust(30))
        print(f'Additionals: {[add.name for add in item.additional_items]}')
        print(f'Notes: {[n for n in item.additional_notes]}')
        print(f"".ljust(self._colsize, '-'))
