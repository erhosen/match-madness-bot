import time

from PIL.Image import Image

from helpers.utils import click, take_screenshot, pixel_matches_color
from screen._base import BaseScreen


class FinishScreen(BaseScreen):
    NEXT_BUTTON = 530, 756

    LOGO_PIXEL = 530, 380

    DUOLINGO_LIGHT_ORANGE = (215, 108, 35)
    DUOLINGO_WHITE = (255, 255, 255)

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return pixel_matches_color(
            cls.LOGO_PIXEL, cls.DUOLINGO_LIGHT_ORANGE, image=screenshot
        ) and pixel_matches_color(cls.NEXT_BUTTON, cls.DUOLINGO_WHITE, image=screenshot)

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.intermediate import IntermediateScreen
        from screen.extreme import ExtremeScreen
        from screen.start import StartScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if IntermediateScreen.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return ExtremeScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        click(*self.NEXT_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen()


if __name__ == "__main__":
    screen = FinishScreen()
    screenshot = take_screenshot()
    is_current = screen.is_current(screenshot)
    print(is_current)
