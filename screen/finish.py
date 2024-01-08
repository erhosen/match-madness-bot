import time

from helpers.utils import click, take_screenshot
from screen.start import StartScreen


class FinishScreen:
    NEXT_BUTTON = 530, 756

    def __init__(self):
        pass

    def next(self):
        from screen.intermediate import IntermediateScreen
        from screen.extreme import ExtremeScreen

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
