import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NEXT_BUTTON_SPRITE = open_image("sprites/next_button.png")


class FinishScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return NEXT_BUTTON_SPRITE in screenshot

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.intermediate import IntermediateScreen
        from screen.extreme import ExtremeScreen
        from screen.start import StartScreen
        from screen.rate_us import RateUsScreen

        for _ in range(30):
            time.sleep(1)
            screenshot = Screenshot.take()

            if IntermediateScreen.is_current(screenshot):
                return IntermediateScreen
            elif RateUsScreen.is_current(screenshot):
                return RateUsScreen
            elif ExtremeScreen.is_current(screenshot):
                return ExtremeScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        Screenshot.take().click_on(NEXT_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()
