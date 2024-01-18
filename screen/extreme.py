import time

from PIL.Image import Image

from helpers.utils import click, pixel_matches_color
from screen._base import BaseScreen


class ExtremeScreen(BaseScreen):
    LOGO_PIXEL = 550, 370
    START_BUTTON = 666, 746

    DUOLINGO_ORANGE = (240, 120, 43)
    DUOLINGO_WHITE = (255, 255, 255)

    @classmethod
    def is_current(cls, screenshot: Image):
        # should have an orange logo in the middle and a white start button
        return pixel_matches_color(
            cls.LOGO_PIXEL, cls.DUOLINGO_ORANGE, image=screenshot
        ) and pixel_matches_color(
            cls.START_BUTTON, cls.DUOLINGO_WHITE, image=screenshot
        )

    def next(self):
        from screen.start import StartScreen

        print("Extreme screen found, clicking start button")
        click(*self.START_BUTTON)
        time.sleep(6)

        return StartScreen()
