from src.structural.facade.domain.card import Card
from src.structural.facade.domain.connect_server import CardServer
from src.structural.facade.domain.payment_method import PaymentMethod
from src.structural.facade.domain.process_payment import ProcessPayment


class PaymentMachine:

    def __init__(self):
        self.server = CardServer()
        self.method = PaymentMethod()
        self.payment_process = ProcessPayment()

    def pay(self, card: Card, cost: float, password_encrypted: str):
        self.server.connect(card)
        self.method.configure(card)
        self.payment_process.set_cost(cost)
        self.payment_process.set_password(password_encrypted)
        self.payment_process.send()
        print("Ok.")
