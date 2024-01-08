import time

from helpers.utils import click
from screen.start import StartScreen


class FinishScreen:
    NEXT_BUTTON = 530, 756

    def __init__(self):
        pass

    def next(self):
        from screen.intermediate import IntermediateScreen

        click(*self.NEXT_BUTTON)
        time.sleep(6)

        if IntermediateScreen.is_current():
            return IntermediateScreen()

        return StartScreen()


if __name__ == "__main__":
    screen = FinishScreen()
    screen.next()
