import time

from PIL.Image import Image

from helpers.utils import take_screenshot, locate_sprite, open_image, click_on
from screen._base import BaseScreen


NOT_NOW_BUTTON_SPRITE = open_image("sprites/not_now_button.png")


class RateUsScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        point = locate_sprite(NOT_NOW_BUTTON_SPRITE, screenshot)
        return bool(point)

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.extreme import ExtremeScreen
        from screen.intermediate import IntermediateScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if IntermediateScreen.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return ExtremeScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        print('Rate us screen found, clicking "Not Now" button')
        click_on(NOT_NOW_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()
