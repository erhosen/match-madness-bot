import time
from functools import partial


from helpers.constants import Language, LEVELS_CONFIG
from helpers.match_madness import MatchMadness, NoTranslationFound
from helpers.screenshot import Screenshot
from screen._base import BaseScreen
from helpers.utils import open_image

EXIT_CROSS_SPRITE = open_image("sprites/exit_cross.png")


class GameScreen(BaseScreen):
    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter

        self.match_madness = MatchMadness(
            lang_left=Language.RUS, lang_right=Language.DEU
        )
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return EXIT_CROSS_SPRITE in screenshot

    def determine_next_screen(self):
        from screen.attention import AttentionScreen
        from screen.timeout import TimeoutScreen
        from screen.wait_where_are_you import WaitWhereAreYouScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = Screenshot.take()

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
            Screenshot.take().click_on(EXIT_CROSS_SPRITE)
            print("No translation found, trying to continue...")

        NextScreen = self.determine_next_screen()
        return NextScreen()
