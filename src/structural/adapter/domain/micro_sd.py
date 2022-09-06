from src.structural.adapter.core.memory_card import MemoryCard


class MicroSD(MemoryCard):

    def __init__(self):
        super().__init__("MicroSD", 8)
