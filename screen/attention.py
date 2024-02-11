import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NEXT_BUTTON_SPRITE = open_image("sprites/next_button.png")


class AttentionScreen(BaseScreen):
    sprite = open_image("sprites/next_button.png")
    next_screens = [
        "FinishScreen",
        "WaitWhereAreYouScreen",
    ]

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    def next(self):
        from screen.game import GameScreen

        print(f"lvl: {self.lvl}, chapter: {self.chapter}")
        Screenshot.take().click_on(NEXT_BUTTON_SPRITE)

        if self.chapter < 3:
            time.sleep(0.4)
            return GameScreen(lvl=self.lvl, chapter=self.chapter)

        NextScreen = self.determine_next_screen()  # noqa
        return NextScreen()  # type: ignore
