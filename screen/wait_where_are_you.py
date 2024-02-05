import time

from PIL.Image import Image

from helpers.utils import take_screenshot, open_image, locate_sprite, click_on
from screen._base import BaseScreen


EXIT_BUTTON_SPRITE = open_image("sprites/exit_button.png")


class WaitWhereAreYouScreen(BaseScreen):
    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        point = locate_sprite(EXIT_BUTTON_SPRITE, screenshot)
        return bool(point)

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.finish import FinishScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if FinishScreen.is_current(screenshot):
                return FinishScreen
            if StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self) -> "BaseScreen":
        click_on(EXIT_BUTTON_SPRITE)

        NextScreen = self.determine_next_screen()
        return NextScreen()


if __name__ == "__main__":
    _screen = WaitWhereAreYouScreen()
    _screenshot = take_screenshot()
    print(_screen.is_current(_screenshot))

    # exit_button_sprite = _screenshot.crop((300, 730, 385, 760))
    # save_image(exit_button_sprite, "sprites/exit_button.png")
