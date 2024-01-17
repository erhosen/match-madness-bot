import time

from PIL.Image import Image

from helpers.utils import click
from screen._base import BaseScreen


class AttentionScreen(BaseScreen):
    NEXT_BUTTON = 730, 746

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return False

    def next(self):
        from screen.game import GameScreen
        from screen.finish import FinishScreen

        print(f"lvl: {self.lvl}, chapter: {self.chapter}")
        click(*self.NEXT_BUTTON)
        time.sleep(0.5)

        if self.chapter < 3:
            return GameScreen(lvl=self.lvl, chapter=self.chapter)
        else:
            time.sleep(17)
            return FinishScreen()
