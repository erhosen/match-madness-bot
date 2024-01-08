import time

from helpers.utils import click
from screen.attention import AttentionScreen
from screen.intermediate import IntermediateScreen


class DoublePointsScreen(IntermediateScreen):
    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    def next(self):
        print("DoublePoints screen found, buying double points 💰")

        click(*self.NEXT_BUTTON)
        time.sleep(4)

        return AttentionScreen(lvl=self.lvl, chapter=self.chapter)
