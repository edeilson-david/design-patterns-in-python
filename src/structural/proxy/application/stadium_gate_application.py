from src.commons.app_runner import AppRunner
from src.structural.proxy.domain.stadium_gate import StadiumGate
from src.structural.proxy.domain.stadium_gate_security import StadiumGateSecurity


class StadiumGateApplication(AppRunner):

    def execute(self, args: list):

        gate = StadiumGateSecurity(StadiumGate())
        gate.open("MEA#65483")
        gate.close()
        gate.open("")


if __name__ == "__main__":
    AppRunner.run(StadiumGateApplication, [])
