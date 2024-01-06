import time

import pyautogui


class AttentionScreen:
    NEXT_BUTTON = 730, 800

    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter

    def next(self):
        from screen.game import GameScreen
        from screen.finish import FinishScreen

        pyautogui.click(*self.NEXT_BUTTON)
        time.sleep(0.5)
        if self.chapter < 3:
            return GameScreen(lvl=self.lvl, chapter=self.chapter)
        else:
            time.sleep(9)
            return FinishScreen()
