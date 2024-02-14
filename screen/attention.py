import time

from helpers.screenshot import Screenshot, Sprite
from screen._base import BaseScreen


NEXT_BUTTON_SPRITE = Sprite.open("next_button.png")


class AttentionScreen(BaseScreen):
    look_for_sprite = Sprite.open("next_button.png")
    click_on_sprite = Sprite.open("next_button.png")
    next_screens = [
        "FinishScreen",
        "WaitWhereAreYouScreen",
    ]

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return screenshot.has_sprite(cls.look_for_sprite, confidence=0.8)

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter
        super().__init__()

    def next(self):
        from screen.game import GameScreen

        print(f"lvl: {self.lvl}, chapter: {self.chapter}")
        Screenshot.take().click_on(NEXT_BUTTON_SPRITE.image)

        if self.chapter < 3:
            time.sleep(0.4)
            return GameScreen(lvl=self.lvl, chapter=self.chapter)

        NextScreen = self.determine_next_screen()  # noqa
        return NextScreen()  # type: ignore


if __name__ == "__main__":
    screen = AttentionScreen(1, 0)
    _screenshot = Screenshot.take()
    print(screen.is_current(_screenshot))
