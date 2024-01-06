import time

import pyautogui
from screen.start import StartScreen


class IntermediateScreen:
    NEXT_BUTTON = 660, 800
    DUOLINGO_BLUE = (70, 182, 243)

    def __init__(self):
        pass

    @classmethod
    def is_current(cls):
        intermediate_button_color = pyautogui.pixel(*cls.NEXT_BUTTON)
        # if screen has blue "next button", it's probably some intermediate screen, like "Rating Up"
        if intermediate_button_color == cls.DUOLINGO_BLUE:
            return True
        return False

    def next(self):
        print("Intermediate screen found, clicking next button")
        pyautogui.click(*self.NEXT_BUTTON)
        time.sleep(6)

        if self.is_current():
            # the next screen is also intermediate, what a surprise
            return IntermediateScreen()

        return StartScreen()
