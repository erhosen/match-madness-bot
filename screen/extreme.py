from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


START_BUTTON_SPRITE = open_image("sprites/start_button.png")


class ExtremeScreen(BaseScreen):
    sprite = open_image("sprites/start_button.png")
    next_screens = [
        "StartScreen",
    ]

    def next(self):
        print("Extreme screen found, clicking start button")
        Screenshot.take().click_on(START_BUTTON_SPRITE)
        NextScreen = self.determine_next_screen()
        return NextScreen()
