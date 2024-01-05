import time

import pyautogui

from screens.start import StartScreen


class FinishScreen:
    NEXT_BUTTON = 530, 810
    INTERMEDIATE_NEXT_BUTTON = 660, 800
    DUOLINGO_BLUE = (70, 182, 243)

    def __init__(self):
        pass

    def next(self):
        pyautogui.click(*self.NEXT_BUTTON)
        time.sleep(6)

        intermediate_button_color = pyautogui.pixel(*self.INTERMEDIATE_NEXT_BUTTON)
        # if screenshot has blue "next button", it's probably some intermediate screen, like "Rating Up"
        if intermediate_button_color == self.DUOLINGO_BLUE:
            print("Intermediate screen found, clicking next button")
            pyautogui.click(*self.INTERMEDIATE_NEXT_BUTTON)
            time.sleep(6)

        return StartScreen()


if __name__ == "__main__":
    screen = FinishScreen()
    screen.next()
