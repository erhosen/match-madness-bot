import time

from helpers.screenshot import Screenshot
from helpers.utils import open_image
from screen._base import BaseScreen


NEXT_BUTTON_SPRITE = open_image("sprites/next_button.png")


class AttentionScreen(BaseScreen):
    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return NEXT_BUTTON_SPRITE in screenshot

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.finish import FinishScreen
        from screen.wait_where_are_you import WaitWhereAreYouScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

            if FinishScreen.is_current(screenshot):
                return FinishScreen
            elif WaitWhereAreYouScreen.is_current(screenshot):
                return WaitWhereAreYouScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        from screen.game import GameScreen

        print(f"lvl: {self.lvl}, chapter: {self.chapter}")
        Screenshot.take().click_on(NEXT_BUTTON_SPRITE)

        if self.chapter < 3:
            time.sleep(0.4)
            return GameScreen(lvl=self.lvl, chapter=self.chapter)

        NextScreen = self.determine_next_screen()
        return NextScreen()
