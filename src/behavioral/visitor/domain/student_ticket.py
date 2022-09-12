from src.behavioral.visitor.core.cashier import Cashier
from src.behavioral.visitor.core.ticket import Ticket


class StudentTicket(Ticket):

    def price(self) -> float:
        return 10.50

    def accept(self, cashier: Cashier):
        return cashier.calculate(self)
