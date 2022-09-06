from src.commons.app_runner import AppRunner
from src.structural.adapter.core.sd_adapter import SDAdapter
from src.structural.adapter.core.sd_reader import SDReader
from src.structural.adapter.domain.nano_sd import NanoSD


class MemoryCardReaderApplication(AppRunner):

    def execute(self, args: list):

        card = NanoSD()
        card_adapted = SDAdapter(card)
        reader = SDReader(card_adapted)
        reader.read()


if __name__ == "__main__":
    AppRunner.run(MemoryCardReaderApplication, [])
