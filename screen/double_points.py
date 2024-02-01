import time

from PIL.Image import Image

from helpers.utils import click, pixel_matches_color
from screen._base import BaseScreen
from screen.attention import AttentionScreen


BUY_DOUBLE_POINTS = True


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
        return pixel_matches_color(cls.NEXT_BUTTON, cls.DUOLINGO_BLUE, image=screenshot)

    def next(self):
        print("DoublePoints screen found")

        if BUY_DOUBLE_POINTS:
            print("Buying double points 💰")
            click(*self.NEXT_BUTTON)
        else:
            print("Declining double points 🙅‍")
            click(*self.DECLINE_BUTTON)

        time.sleep(4)

        return AttentionScreen(lvl=self.lvl, chapter=self.chapter)
