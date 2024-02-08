import time

from helpers.utils import (
    click,
    take_screenshot,
    pixel_matches_color,
    save_image,
    open_image,
    has_sprite,
)
from screen._base import BaseScreen


NEXT_TIME_BUTTON_SPRITE = open_image("sprites/next_time_button.png")


class IntermediateScreen(BaseScreen):
    # NO_BUTTON = 345, 741
    NEXT_BUTTON = 630, 746
    DUOLINGO_BLUE = (70, 182, 243)
    DUOLINGO_LIGHT_BLUE = (108, 190, 243)
    DUOLINGO_BACKGROUND = (21, 30, 34)

    @classmethod
    def is_current(cls, screenshot=None) -> bool:
        # if screen has blue "next button", but doesn't have "no button",
        # it's probably some intermediate screen, like "Rating Up"
        return (
            pixel_matches_color(cls.NEXT_BUTTON, cls.DUOLINGO_BLUE, image=screenshot)
            or pixel_matches_color(
                cls.NEXT_BUTTON, cls.DUOLINGO_LIGHT_BLUE, image=screenshot
            )
            or has_sprite(NEXT_TIME_BUTTON_SPRITE, screenshot)
        )

    @classmethod
    def determine_next_screen(cls) -> type[BaseScreen]:
        from screen.start import StartScreen
        from screen.extreme import ExtremeScreen
        from screen.attention import AttentionScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if cls.is_current(screenshot):
                return IntermediateScreen
            elif ExtremeScreen.is_current(screenshot):
                return AttentionScreen
            elif StartScreen.is_current(screenshot):
                return StartScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        print("Intermediate screen found, clicking next button")
        click(*self.NEXT_BUTTON)

        NextScreen = self.determine_next_screen()
        return NextScreen()


if __name__ == "__main__":
    _screen = IntermediateScreen()
    _screenshot = take_screenshot()
    save_image(_screenshot, "screen/intermediate_8.png")
    _is_current = _screen.is_current(_screenshot)
    print(_is_current)

    # next_time_button_sprite = _screenshot.crop((250, 730, 390, 760))
    # save_image(next_time_button_sprite, "sprites/next_time_button.png")

# TODO: Move PairingScreen out of IntermediateScreen (use NEXT_TIME_BUTTON_SPRITE for it)
