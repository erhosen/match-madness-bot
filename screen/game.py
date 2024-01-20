import time
from functools import partial

from PIL.Image import Image

from helpers.constants import Language, LEVELS_CONFIG
from helpers.match_madness import MatchMadness, NoTranslationFound
from screen._base import BaseScreen
from helpers.utils import (
    take_screenshot,
    pixel_matches_color,
)


class GameScreen(BaseScreen):
    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter

        self.match_madness = MatchMadness(
            lang_left=Language.RUS, lang_right=Language.DEU
        )
        super().__init__()

    EXIT_BUTTON = (115, 28)
    PRESS_PAIRS_TEXT = (221, 145)
    DUOLINGO_WHITE = (255, 255, 255)
    DUOLINGO_GRAY = (88, 102, 110)

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        is_pairs_text_white = pixel_matches_color(
            cls.PRESS_PAIRS_TEXT, cls.DUOLINGO_WHITE, image=screenshot
        )
        is_exit_button_gray = pixel_matches_color(
            cls.EXIT_BUTTON, cls.DUOLINGO_GRAY, image=screenshot
        )
        return is_pairs_text_white and is_exit_button_gray

    def determine_next_screen(self) -> type[BaseScreen] | partial[BaseScreen]:
        from screen.attention import AttentionScreen
        from screen.timeout import TimeoutScreen
        from screen.wait_where_are_you import WaitWhereAreYouScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if AttentionScreen.is_current(screenshot):
                # return partial because we need to pass lvl and chapter
                return partial(AttentionScreen, lvl=self.lvl, chapter=self.chapter + 1)
            elif TimeoutScreen.is_current(screenshot):
                return TimeoutScreen
            elif WaitWhereAreYouScreen.is_current(screenshot):
                return WaitWhereAreYouScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        try:
            self.match_madness.process_chapter(
                iterations=LEVELS_CONFIG[self.lvl][self.chapter]
            )
        except NoTranslationFound:
            print("No translation found, trying to continue...")

        NextScreen = self.determine_next_screen()
        return NextScreen()
