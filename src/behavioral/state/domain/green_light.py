from src.behavioral.state.core.light import Light


class GreenLight(Light):

    def next(self) -> Light:
        from src.behavioral.state.domain.yellow_light import YellowLight
        return YellowLight()

    def action(self) -> None:
        print("GREEN")
