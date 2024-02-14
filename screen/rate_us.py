from helpers.screenshot import Sprite
from screen._base import BaseScreen


class RateUsScreen(BaseScreen):
    look_for_sprite = Sprite.open("not_now_button.png")
    click_on_sprite = Sprite.open("not_now_button.png")
    next_screens = ["StartScreen", "IntermediateScreen", "ExtremeScreen"]
