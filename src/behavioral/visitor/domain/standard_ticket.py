from src.behavioral.visitor.core.cashier import Cashier
from src.behavioral.visitor.core.ticket import Ticket


class StandardTicket(Ticket):

    def price(self) -> float:
        return 19.85

    def accept(self, cashier: Cashier):
        return cashier.calculate(self)
