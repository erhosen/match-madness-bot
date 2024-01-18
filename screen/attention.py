import time

from PIL.Image import Image

from helpers.utils import click, take_screenshot, get_image_pixel
from screen._base import BaseScreen


class AttentionScreen(BaseScreen):
    NEXT_BUTTON = 730, 746
    CENTRAL_PIXEL = 540, 380

    DUOLINGO_ORANGE_1 = (247, 114, 35)
    DUOLINGO_BACKGROUND = (20, 28, 32)

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        next_button_color = get_image_pixel(screenshot, *cls.NEXT_BUTTON)
        central_pixel_color = get_image_pixel(screenshot, *cls.CENTRAL_PIXEL)

        return (
            next_button_color == cls.DUOLINGO_ORANGE_1
            and central_pixel_color == cls.DUOLINGO_BACKGROUND
        )

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.finish import FinishScreen

        for _ in range(10):
            time.sleep(2)
            screenshot = take_screenshot()

            if FinishScreen.is_current(screenshot):
                return FinishScreen

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
    screen = AttentionScreen(lvl=1, chapter=0)
    screenshot = take_screenshot()
    is_current = screen.is_current(screenshot)
    print(is_current)
