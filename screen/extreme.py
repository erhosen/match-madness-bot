import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


START_BUTTON_SPRITE = open_image("sprites/start_button.png")


class ExtremeScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return START_BUTTON_SPRITE in screenshot

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

            if StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        print("Extreme screen found, clicking start button")

        Screenshot.take().click_on(START_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()
