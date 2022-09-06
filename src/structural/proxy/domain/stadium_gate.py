from src.structural.proxy.core.gate import Gate


class StadiumGate(Gate):

    def open(self, credential: str):
        print(f"{'' if credential is None or credential == '' else credential + ':'} Opening the Stadium Gate.")

    def close(self):
        print("Closing the Stadium Gate")
