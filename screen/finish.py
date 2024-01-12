import time

from PIL.Image import Image

from helpers.utils import click, take_screenshot
from screen._base import BaseScreen


class FinishScreen(BaseScreen):
    NEXT_BUTTON = 530, 756

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        raise NotImplementedError

    def next(self):
        from screen.intermediate import IntermediateScreen
        from screen.extreme import ExtremeScreen
        from screen.start import StartScreen

        click(*self.NEXT_BUTTON)
        time.sleep(6)

        if IntermediateScreen.is_current():
            return IntermediateScreen()

        screenshot = take_screenshot()
        if ExtremeScreen.is_current(screenshot):
            return ExtremeScreen()

        return StartScreen()


if __name__ == "__main__":
    screen = FinishScreen()
    screen.next()
