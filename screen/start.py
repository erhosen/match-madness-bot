import time

from helpers.ocr import recognize_number
from helpers.screenshot import Screenshot, Sprite
from screen._base import BaseScreen

BIG_START_BUTTON_SPRITE = Sprite.open("big_start_button.png")


class StartScreen(BaseScreen):
    look_for_sprite = Sprite.open("big_start_button.png")
    click_on_sprite = Sprite.open("big_start_button.png")
    next_screens = ["AttentionScreen", "DoublePointsScreen"]

    @staticmethod
    def determine_lvl(screenshot: Screenshot) -> int:
        lvl1_checkbox = screenshot.crop((230, 475, 260, 500))
        lvl2_checkbox = screenshot.crop((370, 475, 400, 500))
        lvln_checkbox = screenshot.crop((510, 475, 540, 500))
        lvl8_checkbox = screenshot.crop((650, 475, 680, 500))
        lvl9_checkbox = screenshot.crop((790, 475, 820, 500))

        for checkbox in (
            lvl1_checkbox,
            lvl2_checkbox,
            lvln_checkbox,
            lvl8_checkbox,
            lvl9_checkbox,
        ):
            if lvl := recognize_number(checkbox):
                return lvl

        raise ValueError("Can't determine level")

    @classmethod
    def _determine_lvl(cls, attempts=5) -> int:
        for _ in range(attempts):
            screenshot = Screenshot.take()
            try:
                lvl = cls.is_current(screenshot) and cls.determine_lvl(screenshot)
                if not lvl:
                    continue
                return lvl
            except ValueError:
                time.sleep(1.5)
                continue

        raise ValueError("Can't determine level")

    def next(self):
        """Click on start button.

        Wait for next screen.
        """
        lvl = self._determine_lvl()

        print(f"Level {lvl}, let's go!")

        Screenshot.take().click_on(BIG_START_BUTTON_SPRITE.image)

        NextScreen = self.determine_next_screen()  # noqa
        return NextScreen(lvl=lvl, chapter=0)  # type: ignore
