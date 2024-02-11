from helpers.utils import open_image
from screen._base import BaseScreen


class RateUsScreen(BaseScreen):
    sprite = open_image("sprites/not_now_button.png")
    next_screens = ["StartScreen", "IntermediateScreen", "ExtremeScreen"]
