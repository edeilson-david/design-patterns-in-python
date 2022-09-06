from src.commons.app_runner import AppRunner
from src.structural.flyweight.domain.database_connector_factory import DatabaseConnectorFactory


class DatabaseConnectionApplication(AppRunner):

    def execute(self, args: list):
        factory = DatabaseConnectorFactory()

        ora_con = factory.get("oracle")
        ora_con.connect("bob", "4@34&*g*55_#a!")

        self.print_line()

        ora_con2 = factory.get("oracle")
        ora_con2.connect("daisy", "4@34&*g*55_#a!")

        self.print_line()

        ptg_con = factory.get("postgresql")
        ptg_con.connect("jhon", "3%63!sF78%gJKn)_*64!")

        self.print_line()

        my_con = factory.get("mysql")
        my_con.connect("michael", "$2)43Ok13LKA5ssac@4_!")

        self.print_line()

        my_con2 = factory.get("mysql")
        my_con2.connect("matt", "$2)43Ok13LKA5ssac@4_!")

    def print_line(self):
        print("-" * 40)


if __name__ == "__main__":
    AppRunner.run(DatabaseConnectionApplication, [])
