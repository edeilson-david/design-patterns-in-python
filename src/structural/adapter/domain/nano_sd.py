from src.structural.adapter.core.memory_card import MemoryCard


class NanoSD(MemoryCard):

    def __init__(self):
        super().__init__("NanoSD", 6)
