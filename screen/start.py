import time

from PIL.Image import Image

from helpers.ocr import get_number_from_image
from screen._base import BaseScreen
from helpers.utils import click, take_screenshot, pixel_matches_color, save_image


class StartScreen(BaseScreen):
    START_BUTTON = 450, 756

    DUOLINGO_WHITE = (255, 255, 255)

    @staticmethod
    def determine_lvl(screenshot: Image) -> int:
        # invert colors && increase contrast
        # screenshot = screenshot.point(lambda x: (255 - x) * 1.3)

        lvl1_checkbox = screenshot.crop((230, 475, 260, 500))
        lvl2_checkbox = screenshot.crop((370, 475, 400, 500))
        lvln_checkbox = screenshot.crop((510, 475, 540, 500))
        lvl8_checkbox = screenshot.crop((650, 475, 680, 500))
        lvl9_checkbox = screenshot.crop((790, 475, 820, 500))
        # save_image(lvl1_checkbox, "checkbox/lvl1.png")
        # save_image(lvl2_checkbox, "checkbox/lvl2.png")
        # save_image(lvln_checkbox, "checkbox/lvln.png")
        # save_image(lvl8_checkbox, "checkbox/lvl8.png")
        # save_image(lvl9_checkbox, "checkbox/lvl9.png")

        for checkbox in (
            lvl1_checkbox,
            lvl2_checkbox,
            lvln_checkbox,
            lvl8_checkbox,
            lvl9_checkbox,
        ):
            if lvl := get_number_from_image(checkbox):
                return lvl

        raise ValueError("Can't determine level")

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        try:
            # we can determine lvl only if we are on start screen
            cls.determine_lvl(screenshot)
            # if we can determine lvl, one additional check that we have a white start button
            return pixel_matches_color(
                cls.START_BUTTON, cls.DUOLINGO_WHITE, image=screenshot
            )
        except ValueError:
            return False

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.double_points import DoublePointsScreen
        from screen.attention import AttentionScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if DoublePointsScreen.is_current(screenshot):
                return DoublePointsScreen
            elif AttentionScreen.is_current(screenshot):
                return AttentionScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        """Click on start button.

        Wait for next screen.
        """
        time.sleep(1)
        screenshot = take_screenshot()
        lvl = self.determine_lvl(screenshot)
        if lvl == 2:
            save_image(screenshot, f"screen/start_{lvl}.png")
        print(f"Level {lvl}, let's go!")

        click(*self.START_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen(lvl=lvl, chapter=0)
