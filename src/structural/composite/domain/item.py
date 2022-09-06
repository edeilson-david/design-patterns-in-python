from src.structural.composite.core.menu_component import MenuComponent


class Item(MenuComponent):

    def __init__(self, label: str):
        super().__init__(label)
