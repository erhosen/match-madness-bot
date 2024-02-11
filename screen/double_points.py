from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


BUY_DOUBLE_POINTS = False

NO_THANKS_BUTTON_SPRITE = open_image("sprites/no_thanks_button.png")
BUY_DOUBLE_POINTS_BUTTON_SPRITE = open_image("sprites/buy_double_points_button.png")


class DoublePointsScreen(BaseScreen):
    sprite = open_image("sprites/buy_double_points_button.png")
    next_screens = [
        "AttentionScreen",
    ]

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    def next(self):
        print("DoublePoints screen found")

        screenshot = Screenshot.take()
        if BUY_DOUBLE_POINTS:
            print("Buying double points 💰")
            screenshot.click_on(BUY_DOUBLE_POINTS_BUTTON_SPRITE)
        else:
            print("Declining double points 🙅‍")
            screenshot.click_on(NO_THANKS_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()  # noqa
        return NextScreen(lvl=self.lvl, chapter=self.chapter)  # type: ignore
