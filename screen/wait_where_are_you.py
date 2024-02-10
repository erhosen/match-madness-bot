import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


EXIT_BUTTON_SPRITE = open_image("sprites/exit_button.png")


class WaitWhereAreYouScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return EXIT_BUTTON_SPRITE in screenshot

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.finish import FinishScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

            if FinishScreen.is_current(screenshot):
                return FinishScreen
            if StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self) -> "BaseScreen":
        Screenshot.take().click_on(EXIT_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()
