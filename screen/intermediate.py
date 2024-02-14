from helpers.screenshot import Screenshot, Sprite
from screen._base import BaseScreen


NEXT_TIME_BUTTON_SPRITE = Sprite.open("next_time_button.png")
CONTINUE_BUTTON_SPRITE = Sprite.open("continue_button.png")
NEXT_BUTTON_SPRITE = Sprite.open("next_button.png")


class IntermediateScreen(BaseScreen):
    next_screens = ["StartScreen", "IntermediateScreen", "ExtremeScreen"]

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        return (
            screenshot.has_sprite(NEXT_TIME_BUTTON_SPRITE)
            or screenshot.has_sprite(CONTINUE_BUTTON_SPRITE)
            or screenshot.has_sprite(NEXT_BUTTON_SPRITE)
        )

    def next(self):
        print("Intermediate screen found, clicking next button")
        Screenshot.take().click_on(CONTINUE_BUTTON_SPRITE.image)
        NextScreen = self.determine_next_screen()
        return NextScreen()


# TODO: Move PairingScreen out of IntermediateScreen (use NEXT_TIME_BUTTON_SPRITE for it)
