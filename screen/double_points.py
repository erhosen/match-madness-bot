import time

from helpers.utils import click, take_screenshot, save_image
from screen._base import BaseScreen
from screen.attention import AttentionScreen


BUY_DOUBLE_POINTS = True


class DoublePointsScreen(BaseScreen):
    NEXT_BUTTON = 630, 746
    DECLINE_BUTTON = 340, 746

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot=None) -> bool:
        return False

    def next(self):
        print("DoublePoints screen found")
        screenshot = take_screenshot()
        save_image(screenshot, "screen/double_points.png")

        if BUY_DOUBLE_POINTS:
            print("Buying double points 💰")
            click(*self.NEXT_BUTTON)
        else:
            print("Declining double points 🙅‍")
            click(*self.DECLINE_BUTTON)

        time.sleep(4)

        return AttentionScreen(lvl=self.lvl, chapter=self.chapter)
