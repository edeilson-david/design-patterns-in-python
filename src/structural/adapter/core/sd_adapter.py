import time

from src.structural.adapter.core.memory_card import MemoryCard
from src.structural.adapter.domain.sd import SD


class SDAdapter(SD):

    def __init__(self, source: MemoryCard):
        super().__init__()

        if isinstance(source, SD):
            raise Exception("Not is possible adapter SD to SD.")

        print(f"Original card name: {source.name}")
        print(f"Original card pins: {source.pins}")

        print("Adapting card...")
        time.sleep(10)

        print(f"Card adapted to: {self.name}")
        print(f"Card pins: {self.pins}")
