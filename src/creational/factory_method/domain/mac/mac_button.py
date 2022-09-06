from src.creational.factory_method.core.button import Button


class MacButton(Button):

    def render(self) -> None:
        print('Render the OK button on MAC.')

    def on_click(self) -> None:
        print('The OK button was clicked on MAC.')
