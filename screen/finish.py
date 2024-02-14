from helpers.screenshot import Sprite
from screen._base import BaseScreen


class FinishScreen(BaseScreen):
    look_for_sprite = Sprite.open("next_button.png")
    click_on_sprite = Sprite.open("next_button.png")
    next_screens = [
        "StartScreen",
        "IntermediateScreen",
        "ExtremeScreen",
        "RateUsScreen",
    ]
