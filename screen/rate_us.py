import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NOT_NOW_BUTTON_SPRITE = open_image("sprites/not_now_button.png")


class RateUsScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return NOT_NOW_BUTTON_SPRITE in screenshot

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.extreme import ExtremeScreen
        from screen.intermediate import IntermediateScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

            if IntermediateScreen.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return ExtremeScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        print('Rate us screen found, clicking "Not Now" button')
        Screenshot.take().click_on(NOT_NOW_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()
