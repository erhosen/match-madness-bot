import time

from PIL.Image import Image

from helpers.utils import (
    click,
    take_screenshot,
    pixel_matches_color,
    open_image,
    locate_sprite,
)
from screen._base import BaseScreen


NEXT_BUTTON_GREEN_SPRITE = open_image("sprites/next_button_green.png")


class AttentionScreen(BaseScreen):
    NEXT_BUTTON = 730, 746
    CENTRAL_PIXEL = 540, 380

    DUOLINGO_RED = (254, 113, 109)
    DUOLINGO_GREEN = (161, 209, 81)
    DUOLINGO_ORANGE = (240, 120, 43)
    DUOLINGO_BACKGROUND = (21, 30, 34)

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        point = locate_sprite(NEXT_BUTTON_GREEN_SPRITE, screenshot)
        return (
            pixel_matches_color(cls.NEXT_BUTTON, cls.DUOLINGO_ORANGE, image=screenshot)
            or bool(point)
            or pixel_matches_color(
                cls.NEXT_BUTTON, cls.DUOLINGO_RED, image=screenshot, threshold=20
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


if __name__ == "__main__":
    _screen = AttentionScreen(lvl=12, chapter=1)
    _screenshot = take_screenshot()
    _is_current = _screen.is_current(_screenshot)
    print(_is_current)

    # next_button_green_sprite = _screenshot.crop((660, 725, 920, 765))
    # save_image(next_button_green_sprite, "sprites/next_button_green.png")
