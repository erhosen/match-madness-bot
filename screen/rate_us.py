from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NOT_NOW_BUTTON_SPRITE = open_image("sprites/not_now_button.png")


class RateUsScreen(BaseScreen):
    sprite = open_image("sprites/not_now_button.png")
    next_screens = ["StartScreen", "IntermediateScreen", "ExtremeScreen"]

    def next(self):
        print('Rate us screen found, clicking "Not Now" button')
        Screenshot.take().click_on(NOT_NOW_BUTTON_SPRITE)
        NextScreen = self.determine_next_screen()
        return NextScreen()
