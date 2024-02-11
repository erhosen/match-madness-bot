from helpers.constants import Language, LEVELS_CONFIG
from helpers.match_madness import MatchMadness, NoTranslationFound
from helpers.screenshot import Screenshot
from screen._base import BaseScreen
from helpers.utils import open_image

EXIT_CROSS_SPRITE = open_image("sprites/exit_cross.png")


class GameScreen(BaseScreen):
    sprite = open_image("sprites/exit_cross.png")
    next_screens = ["AttentionScreen", "TimeoutScreen", "WaitWhereAreYouScreen"]

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter

        self.match_madness = MatchMadness(
            lang_left=Language.RUS, lang_right=Language.DEU
        )
        super().__init__()

    def next(self):
        try:
            self.match_madness.process_chapter(
                iterations=LEVELS_CONFIG[self.lvl][self.chapter]
            )
        except NoTranslationFound:
            Screenshot.take().click_on(EXIT_CROSS_SPRITE)
            print("No translation found, trying to continue...")

        NextScreen = self.determine_next_screen()  # noqa
        if NextScreen.__name__ == "AttentionScreen":
            return NextScreen(lvl=self.lvl, chapter=self.chapter + 1)  # type: ignore

        return NextScreen()  # type: ignore
