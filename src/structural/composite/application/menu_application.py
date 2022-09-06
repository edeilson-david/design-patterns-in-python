from src.commons.app_runner import AppRunner
from src.structural.composite.domain.item import Item
from src.structural.composite.domain.subitem import SubItem


class MenuApplication(AppRunner):

    def execute(self, args: list):

        edit = SubItem("Edit")
        edit.append(Item("Copy"))
        edit.append(Item("Paste"))

        about = Item("About")
        help = Item("Help")

        toolbar = [edit, about, help]

        for item in toolbar:
            item.render()


if __name__ == "__main__":
    AppRunner.run(MenuApplication, [])
