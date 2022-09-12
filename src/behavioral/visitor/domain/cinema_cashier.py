from src.behavioral.visitor.core.cashier import Cashier


class CinemaCashier(Cashier):

    def calculate(self, ticket):
        price = ticket.price()
        print(f"Ticket cost: {price}")
