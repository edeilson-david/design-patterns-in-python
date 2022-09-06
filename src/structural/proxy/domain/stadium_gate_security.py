from src.structural.proxy.core.gate import Gate


class StadiumGateSecurity(Gate):

    def __init__(self, gate: Gate):
        self._gate = gate

    def open(self, credential: str):
        if credential is None or "" == credential:
            print("You can't openning the Stadium Gate.")
            return

        self._gate.open(credential)

    def close(self):
        self._gate.close()
