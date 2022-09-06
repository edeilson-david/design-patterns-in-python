import time

from src.structural.facade.domain.connect_server import CardServer


class ProcessPayment:

    def __init__(self):
        self.cost = None
        self.password_encrypted = None

    def send(self):
        print("Processing payment...")
        time.sleep(3)

    def set_cost(self, cost: float) -> None:
        print(f"Cost: {cost}")
        self.cost = cost

    def set_password(self, password_encrypted) -> None:
        print(f"Password: ******")
        self.password_encrypted = password_encrypted
