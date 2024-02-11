from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NO_THANKS_BUTTON_SPRITE = open_image("sprites/no_thanks_button.png")


class TimeoutScreen(BaseScreen):
    sprite = open_image("sprites/no_thanks_button.png")
    next_screens = ["StartScreen", "WaitWhereAreYouScreen"]

    def next(self) -> "BaseScreen":
        print('Timeout screen found, clicking "no thanks" button')
        Screenshot.take().click_on(NO_THANKS_BUTTON_SPRITE)
        NextScreen = self.determine_next_screen()
        return NextScreen()
