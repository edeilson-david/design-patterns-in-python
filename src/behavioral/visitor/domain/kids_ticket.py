from src.behavioral.visitor.core.cashier import Cashier
from src.behavioral.visitor.core.ticket import Ticket


class KidsTicket(Ticket):

    def price(self) -> float:
        return 6.20

    def accept(self, cashier: Cashier):
        return cashier.calculate(self)
