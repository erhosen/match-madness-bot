from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NEXT_TIME_BUTTON_SPRITE = open_image("sprites/next_time_button.png")
CONTINUE_BUTTON_SPRITE = open_image("sprites/continue_button.png")
NEXT_BUTTON_SPRITE = open_image("sprites/next_button.png")


class IntermediateScreen(BaseScreen):
    next_screens = ["StartScreen", "IntermediateScreen", "ExtremeScreen"]

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return (
            NEXT_TIME_BUTTON_SPRITE in screenshot
            or CONTINUE_BUTTON_SPRITE in screenshot
            or NEXT_BUTTON_SPRITE in screenshot
        )

    def next(self):
        print("Intermediate screen found, clicking next button")
        Screenshot.take().click_on(CONTINUE_BUTTON_SPRITE)
        NextScreen = self.determine_next_screen()
        return NextScreen()


# TODO: Move PairingScreen out of IntermediateScreen (use NEXT_TIME_BUTTON_SPRITE for it)
