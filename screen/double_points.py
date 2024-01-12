import time

from helpers.utils import click
from screen.attention import AttentionScreen
from screen.intermediate import IntermediateScreen


BUY_DOUBLE_POINTS = False


class DoublePointsScreen(IntermediateScreen):
    DECLINE_BUTTON = 340, 746
    # NEXT_BUTTON = 630, 746

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

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
