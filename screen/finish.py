import time

from PIL.Image import Image

from helpers.utils import click, take_screenshot, get_image_pixel
from screen._base import BaseScreen


class FinishScreen(BaseScreen):
    NEXT_BUTTON = 530, 756

    LOGO_PIXEL = 530, 380

    DUOLINGO_ORANGE_1 = (218, 102, 31)
    DUOLINGO_WHITE = (255, 255, 255)

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        logo_color = get_image_pixel(screenshot, *cls.LOGO_PIXEL)
        start_button_color = get_image_pixel(screenshot, *cls.NEXT_BUTTON)

        return (
            logo_color in [cls.DUOLINGO_ORANGE_1]
            and start_button_color == cls.DUOLINGO_WHITE
        )

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.intermediate import IntermediateScreen
        from screen.extreme import ExtremeScreen
        from screen.start import StartScreen

        for _ in range(10):
            time.sleep(2)
            screenshot = take_screenshot()

            if IntermediateScreen.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return ExtremeScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        click(*self.NEXT_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen()


if __name__ == "__main__":
    screen = FinishScreen()
    screenshot = take_screenshot()
    is_current = screen.is_current(screenshot)
    print(is_current)
