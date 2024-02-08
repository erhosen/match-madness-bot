import time

from PIL.Image import Image

from helpers.utils import open_image, click_on, has_sprite
from screen._base import BaseScreen


BUY_DOUBLE_POINTS = True

NO_THANKS_BUTTON_SPRITE = open_image("sprites/no_thanks_button.png")
BUY_DOUBLE_POINTS_BUTTON_SPRITE = open_image("sprites/buy_double_points_button.png")


class DoublePointsScreen(BaseScreen):
    NEXT_BUTTON = 630, 746
    DECLINE_BUTTON = 340, 746

    DUOLINGO_BLUE = (107, 190, 243)

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return has_sprite(BUY_DOUBLE_POINTS_BUTTON_SPRITE, screenshot) and has_sprite(
            NO_THANKS_BUTTON_SPRITE, screenshot
        )

    def next(self):
        from screen.attention import AttentionScreen

        print("DoublePoints screen found")

        if BUY_DOUBLE_POINTS:
            print("Buying double points 💰")
            click_on(BUY_DOUBLE_POINTS_BUTTON_SPRITE)
        else:
            print("Declining double points 🙅‍")
            click_on(NO_THANKS_BUTTON_SPRITE)

        time.sleep(4)

        return AttentionScreen(lvl=self.lvl, chapter=self.chapter)


if __name__ == "__main__":
    _screen = DoublePointsScreen(1, 1)
    _screenshot = open_image("screen/_double_points.png")
    _is_current = _screen.is_current(_screenshot)
    print(_is_current)

    # buy_double_points_button = _screenshot.crop((580, 730, 840, 760))
    # save_image(buy_double_points_button, "sprites/buy_double_points_button.png")
