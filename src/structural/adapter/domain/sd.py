from src.structural.adapter.core.memory_card import MemoryCard


class SD(MemoryCard):

    def __init__(self):
        super().__init__("SD", 9)
