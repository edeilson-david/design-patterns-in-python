from src.creational.factory_method.core.button import Button
from src.creational.factory_method.core.dialog import Dialog
from src.creational.factory_method.domain.windows.windows_button import WindowsButton


class WindowsDialog(Dialog):

    def createButton(self) -> Button:
        return WindowsButton()
