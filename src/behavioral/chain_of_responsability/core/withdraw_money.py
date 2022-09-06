from __future__ import annotations

import abc


class WithdrawMoney(abc.ABC):

    @abc.abstractmethod
    def set_next(self, withdraw_money: WithdrawMoney) -> WithdrawMoney:
        pass

    @abc.abstractmethod
    def withdraw_money(self, amount: int) -> int:
        pass
