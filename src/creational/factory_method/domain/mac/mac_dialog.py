from src.creational.factory_method.core.button import Button
from src.creational.factory_method.core.dialog import Dialog
from src.creational.factory_method.domain.mac.mac_button import MacButton


class MacDialog(Dialog):

    def createButton(self) -> Button:
        return MacButton()
