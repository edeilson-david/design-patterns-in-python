from src.structural.adapter.domain.sd import SD


class SDReader:

    def __init__(self, sd: SD):
        self._sd = sd

    def read(self) -> None:
        print("Starting reading..")
        print(f"Card name: {self._sd.name}")
        print(f"Card pins: {self._sd.pins}")
        print(f"Reading content...")
