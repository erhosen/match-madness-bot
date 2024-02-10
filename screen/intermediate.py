import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NEXT_TIME_BUTTON_SPRITE = open_image("sprites/next_time_button.png")
CONTINUE_BUTTON_SPRITE = open_image("sprites/continue_button.png")
NEXT_BUTTON_SPRITE = open_image("sprites/next_button.png")


class IntermediateScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return (
            NEXT_TIME_BUTTON_SPRITE in screenshot
            or CONTINUE_BUTTON_SPRITE in screenshot
            or NEXT_BUTTON_SPRITE in screenshot
        )

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.extreme import ExtremeScreen
        from screen.attention import AttentionScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

            if cls.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return AttentionScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        print("Intermediate screen found, clicking next button")
        Screenshot.take().click_on(CONTINUE_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()


# TODO: Move PairingScreen out of IntermediateScreen (use NEXT_TIME_BUTTON_SPRITE for it)
