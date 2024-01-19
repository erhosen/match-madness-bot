import time

from PIL.Image import Image

from helpers.utils import take_screenshot, pixel_matches_color, click
from screen._base import BaseScreen


class TimeoutScreen(BaseScreen):
    USE_HINT_BUTTON = 400, 710
    IGNORE_BUTTON = 400, 755
    EXIT_BUTTON = 340, 745

    DUOLINGO_LIGHT_BLUE = (108, 190, 243)
    DUOLINGO_BACKGROUND = (21, 30, 34)

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return pixel_matches_color(
            cls.USE_HINT_BUTTON, cls.DUOLINGO_LIGHT_BLUE, image=screenshot
        ) and pixel_matches_color(
            cls.IGNORE_BUTTON, cls.DUOLINGO_BACKGROUND, image=screenshot
        )

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self) -> "BaseScreen":
        print("Timeout screen found, clicking ignore button")
        click(*self.IGNORE_BUTTON)

        time.sleep(2)

        print("Wait, where are you going?")
        click(*self.EXIT_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen()
