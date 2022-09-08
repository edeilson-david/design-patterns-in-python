from src.behavioral.state.core.light import Light


class YellowLight(Light):

    def next(self) -> Light:
        from src.behavioral.state.domain.red_light import RedLight
        return RedLight()

    def action(self) -> None:
        print("YELLOW")
