from src.behavioral.state.core.light import Light


class RedLight(Light):

    def next(self) -> Light:
        from src.behavioral.state.domain.green_light import GreenLight
        return GreenLight()

    def action(self) -> None:
        print("RED")

