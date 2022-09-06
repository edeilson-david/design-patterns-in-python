from src.creational.factory_method.core.button import Button


class WindowsButton(Button):

    def render(self) -> None:
        print('Render the OK button on WINDOWS.')

    def on_click(self) -> None:
        print('The OK button was clicked on WINDOWS.')
