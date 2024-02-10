import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NO_THANKS_BUTTON_SPRITE = open_image("sprites/no_thanks_button.png")


class TimeoutScreen(BaseScreen):
    IGNORE_BUTTON = 400, 755
    EXIT_BUTTON = 340, 745

    DUOLINGO_LIGHT_BLUE = (108, 190, 243)
    DUOLINGO_BACKGROUND = (21, 30, 34)

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return NO_THANKS_BUTTON_SPRITE in screenshot

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.wait_where_are_you import WaitWhereAreYouScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

            if StartScreen.is_current(screenshot):
                return StartScreen
            elif WaitWhereAreYouScreen.is_current(screenshot):
                return WaitWhereAreYouScreen

        raise ValueError("Can't determine next screen")

    def next(self) -> "BaseScreen":
        print('Timeout screen found, clicking "no thanks" button')
        Screenshot.take().click_on(NO_THANKS_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()
