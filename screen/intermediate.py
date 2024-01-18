import time

from helpers.utils import click, get_pixel, take_screenshot
from screen._base import BaseScreen


class IntermediateScreen(BaseScreen):
    NEXT_BUTTON = 630, 746
    DUOLINGO_BLUE_1 = (70, 182, 243)
    DUOLINGO_BLUE_2 = (108, 190, 243)
    DUOLINGO_BLUE_3 = (107, 190, 243)

    @classmethod
    def is_current(cls, screenshot=None) -> bool:
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

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.extreme import ExtremeScreen
        from screen.attention import AttentionScreen

        for _ in range(5):
            time.sleep(3)
            screenshot = take_screenshot()

            if cls.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return AttentionScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        print("Intermediate screen found, clicking next button")
        click(*self.NEXT_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen()


if __name__ == "__main__":
    is_current = IntermediateScreen().is_current()
    print(is_current)
