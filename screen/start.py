import time

from helpers.ocr import get_number_from_image
from screen.attention import AttentionScreen
from helpers.utils import take_screenshot, click, save_image


class StartScreen:
    START_BUTTON = 530, 756

    def __init__(self):
        self.screenshot = take_screenshot()
        save_image(self.screenshot, "screen/start.png")

    def determine_lvl(self) -> int:
        # invert colors && increase contrast
        screenshot = self.screenshot.convert("L")
        screenshot = screenshot.point(lambda x: (255 - x) * 1.3)

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

    def next(self):
        """Click on start button.

        Wait for next screen.
        """
        lvl = self.determine_lvl()
        print(f"Starting with lvl {lvl}")

        click(*self.START_BUTTON)
        time.sleep(4)
        return AttentionScreen(lvl=lvl, chapter=0)


# TODO: StartSceen -> AttentionScreen -> GameScreen
# TODO: StartSceen -> InermediateScreen -> AttentionScreen -> GameScreen
