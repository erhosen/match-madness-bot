import time

import pyautogui
from pytesseract import pytesseract

from screens.attention import AttentionScreen
from utils import take_screenshot


class StartScreen:
    START_BUTTON = 530, 810
    # START_BUTTON_MAC = 530, 830

    def __init__(self):
        self.screenshot = take_screenshot()
        self.screenshot.save("img/screen/start.png")

    def determine_lvl(self) -> int:
        # screenshot = self.screenshot.convert('L')
        # invert colors && increase contrast
        screenshot = self.screenshot.convert("L")
        screenshot = screenshot.point(lambda x: (255 - x) * 1.5)

        lvl1_checkbox = screenshot.crop((230, 475, 260, 500))
        # lvl1_checkbox.save('img/checkbox/lvl1.png')
        lvl2_checkbox = screenshot.crop((370, 475, 400, 500))
        lvln_checkbox = screenshot.crop((510, 475, 540, 500))
        lvln_checkbox.save("img/checkbox/lvln.png")
        lvl8_checkbox = screenshot.crop((650, 475, 680, 500))
        lvl8_checkbox.save("img/checkbox/lvl8.png")
        lvl9_checkbox = screenshot.crop((790, 475, 820, 500))
        lvl9_checkbox.save("img/checkbox/lvl9.png")

        for checkbox in (
            lvl1_checkbox,
            lvl2_checkbox,
            lvln_checkbox,
            lvl8_checkbox,
            lvl9_checkbox,
        ):
            try:
                lvl_str = pytesseract.image_to_string(
                    checkbox, config="--psm 7 -c tessedit_char_whitelist=01234567899"
                )
                return int(lvl_str)
            except ValueError:
                pass

        raise ValueError("Can't determine level")

    def next(self):
        """Click on start button.

        Wait for next screen.
        """
        lvl = self.determine_lvl()
        print(f"Starting with lvl {lvl}")

        pyautogui.click(*self.START_BUTTON)
        time.sleep(4)
        return AttentionScreen(lvl=lvl, chapter=0)
