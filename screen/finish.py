from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NEXT_BUTTON_SPRITE = open_image("sprites/next_button.png")


class FinishScreen(BaseScreen):
    sprite = open_image("sprites/next_button.png")
    next_screens = [
        "StartScreen",
        "IntermediateScreen",
        "ExtremeScreen",
        "RateUsScreen",
    ]

    def next(self):
        Screenshot.take().click_on(NEXT_BUTTON_SPRITE)
        NextScreen = self.determine_next_screen()
        return NextScreen()
