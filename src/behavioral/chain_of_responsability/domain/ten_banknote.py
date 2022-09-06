from __future__ import annotations
from src.behavioral.chain_of_responsability.core.withdraw_money import WithdrawMoney


class TenBanknote(WithdrawMoney):

    def __init__(self):
        self._next = None

    def set_next(self, withdraw_money: WithdrawMoney) -> WithdrawMoney:
        self._next = withdraw_money
        return withdraw_money

    def withdraw_money(self, amount: int):
        base = 10
        notes = int(amount / base)
        print(f"Ten banknotes: {notes}")

        new_amount = amount % base

        if self._next is None:
            return

        self._next.withdraw_money(new_amount)
