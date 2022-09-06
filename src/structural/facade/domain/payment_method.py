from src.structural.facade.domain.card import Card


class PaymentMethod:

    def configure(self, card: Card) -> None:
        method = card.payment_method

        if method is None:
            raise Exception("Payment method is not defined.")

        if "debit" == method:
            print(f"Payment Method: {method}")
            return

        if "credit" == method:
            print(f"Payment Method: {method}")
            return

        raise Exception("The payment method is not supported.")
