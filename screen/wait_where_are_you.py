from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


EXIT_BUTTON_SPRITE = open_image("sprites/exit_button.png")


class WaitWhereAreYouScreen(BaseScreen):
    sprite = open_image("sprites/exit_button.png")
    next_screens = ["StartScreen", "FinishScreen"]

    def next(self) -> "BaseScreen":
        Screenshot.take().click_on(EXIT_BUTTON_SPRITE)
        NextScreen = self.determine_next_screen()
        return NextScreen()
