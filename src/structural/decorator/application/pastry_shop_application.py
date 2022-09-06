from src.commons.app_runner import AppRunner
from src.structural.decorator.core.pastry import Pastry
from src.structural.decorator.domain.bacon import Bacon
from src.structural.decorator.domain.mini_cheese_pastry import MiniCheesePastry
from src.structural.decorator.domain.tomate import Tomate


class PastryShopApplication(AppRunner):

    def execute(self, args: list):
        PastryShopApplication.details(MiniCheesePastry())
        PastryShopApplication.details(Bacon(MiniCheesePastry()))
        PastryShopApplication.details(Tomate(Bacon(MiniCheesePastry())))

    @staticmethod
    def details(pastry: Pastry):
        bar_size = 13 + len(pastry.get_ingredients())
        bar = ("=" * bar_size)
        print(bar)
        print(f"Ingredients: {pastry.get_ingredients()}")
        print(f"Cost: {pastry.get_cost()}")
        print(f"Tax: {pastry.get_tax()}")


if __name__ == "__main__":
    AppRunner.run(PastryShopApplication, [])
