import time

from src.structural.facade.domain.card import Card


class CardServer:

    def connect(self, card: Card):
        print(f"Connecting to card server: {card.company_name}")
        time.sleep(3)
