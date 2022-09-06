from src.commons.app_runner import AppRunner
from src.creational.factory_method.core.dialog import Dialog
from src.creational.factory_method.core.environment import Environment
from src.creational.factory_method.domain.mac.mac_dialog import MacDialog
from src.creational.factory_method.domain.windows.windows_dialog import WindowsDialog


class DialogApplication(AppRunner):

    def execute(self, args: list):
        environment = Environment.get(args[0])
        dialog = DialogApplication._create_dialog(environment)
        button = dialog.createButton()
        button.render()
        button.on_click()

    @staticmethod
    def _create_dialog(environment: Environment) -> Dialog:
        if environment is Environment.WINDOWS:
            return WindowsDialog()

        if environment is Environment.MAC:
            return MacDialog()


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if 0 == len(args):
        args = ["mac"]

    AppRunner.run(DialogApplication, args)
