from src.behavioral.chain_of_responsability.domain.fifty_banknote import FiftyBanknote
from src.behavioral.chain_of_responsability.domain.five_banknote import FiveBanknote
from src.behavioral.chain_of_responsability.domain.hundred_banknote import HundredBanknote
from src.behavioral.chain_of_responsability.domain.one_banknote import OneBanknote
from src.behavioral.chain_of_responsability.domain.ten_banknote import TenBanknote
from src.behavioral.chain_of_responsability.domain.two_banknote import TwoBanknote
from src.commons.app_runner import AppRunner


class ATMMachineApplication(AppRunner):

    def execute(self, args: list):
        cashier = HundredBanknote()
        (cashier
         .set_next(FiftyBanknote())
         .set_next(TenBanknote())
         .set_next(FiveBanknote())
         .set_next(TwoBanknote())
         .set_next(OneBanknote()))

        cashier.withdraw_money(1753)


if __name__ == "__main__":
    AppRunner.run(ATMMachineApplication, [])
