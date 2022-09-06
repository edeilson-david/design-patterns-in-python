from src.commons.app_runner import AppRunner
from src.structural.facade.domain.card import Card
from src.structural.facade.domain.payment_machine import PaymentMachine


class PastryCookApplication(AppRunner):

    def execute(self, args: list):
        card = Card("Visa", "debit")

        machine = PaymentMachine()
        machine.pay(card, 22.75, "$#3fD56#2eFhB_9&$2!%Kç@")


if __name__ == "__main__":
    AppRunner.run(PastryCookApplication, [])
