import time

from PIL.Image import Image

from helpers.utils import click, take_screenshot, pixel_matches_color
from screen._base import BaseScreen


class AttentionScreen(BaseScreen):
    NEXT_BUTTON = 730, 746
    CENTRAL_PIXEL = 540, 380

    DUOLINGO_RED = (254, 113, 109)
    DUOLINGO_GREEN = (134, 203, 62)
    DUOLINGO_ORANGE = (240, 120, 43)
    DUOLINGO_BACKGROUND = (21, 30, 34)

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return (
            pixel_matches_color(cls.NEXT_BUTTON, cls.DUOLINGO_ORANGE, image=screenshot)
            or pixel_matches_color(
                cls.NEXT_BUTTON, cls.DUOLINGO_GREEN, image=screenshot
            )
            or pixel_matches_color(cls.NEXT_BUTTON, cls.DUOLINGO_RED, image=screenshot)
            and pixel_matches_color(
                cls.CENTRAL_PIXEL, cls.DUOLINGO_BACKGROUND, image=screenshot
            )
        )

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.finish import FinishScreen
        from screen.wait_where_are_you import WaitWhereAreYouScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if FinishScreen.is_current(screenshot):
                return FinishScreen
            elif WaitWhereAreYouScreen.is_current(screenshot):
                return WaitWhereAreYouScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        from screen.game import GameScreen

        print(f"lvl: {self.lvl}, chapter: {self.chapter}")
        click(*self.NEXT_BUTTON)

        if self.chapter < 3:
            time.sleep(0.4)
            return GameScreen(lvl=self.lvl, chapter=self.chapter)

        NextScreen = self.determine_next_screen()
        return NextScreen()
