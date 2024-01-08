import time

from helpers.utils import click, get_pixel, take_screenshot
from screen.start import StartScreen


class IntermediateScreen:
    NEXT_BUTTON = 630, 746
    DUOLINGO_BLUE_1 = (70, 182, 243)
    DUOLINGO_BLUE_2 = (108, 190, 243)
    DUOLINGO_BLUE_3 = (107, 190, 243)

    def __init__(self):
        pass

    @classmethod
    def is_current(cls):
        intermediate_button_color = get_pixel(*cls.NEXT_BUTTON)
        # print(f"intermediate_button_color: {intermediate_button_color}")
        # if screen has blue "next button", it's probably some intermediate screen, like "Rating Up"
        if intermediate_button_color in (
            cls.DUOLINGO_BLUE_1,
            cls.DUOLINGO_BLUE_2,
            cls.DUOLINGO_BLUE_3,
        ):
            return True
        return False

    def next(self):
        from screen.extreme import ExtremeScreen

        print("Intermediate screen found, clicking next button")
        click(*self.NEXT_BUTTON)
        time.sleep(6)

        if self.is_current():
            # the next screen is also intermediate, what a surprise
            return IntermediateScreen()

        screenshot = take_screenshot()
        if ExtremeScreen.is_current(screenshot):
            return ExtremeScreen()

        return StartScreen()


if __name__ == "__main__":
    is_current = IntermediateScreen().is_current()
    print(is_current)
