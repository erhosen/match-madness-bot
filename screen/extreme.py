from helpers.screenshot import Sprite
from screen._base import BaseScreen


class ExtremeScreen(BaseScreen):
    look_for_sprite = Sprite.open("extreme_logo.png")
    click_on_sprite = Sprite.open("start_button.png")
    next_screens = [
        "StartScreen",
    ]
