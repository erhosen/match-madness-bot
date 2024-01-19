import time

from PIL.Image import Image

from helpers.utils import take_screenshot, pixel_matches_color, click
from screen._base import BaseScreen


class WaitWhereAreYouScreen(BaseScreen):
    EXIT_BUTTON = 345, 741

    DUOLINGO_RED = (225, 98, 93)

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return pixel_matches_color(cls.EXIT_BUTTON, cls.DUOLINGO_RED, image=screenshot)

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
        click(*self.EXIT_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen()
