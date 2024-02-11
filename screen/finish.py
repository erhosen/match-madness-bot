from helpers.utils import open_image
from screen._base import BaseScreen


class FinishScreen(BaseScreen):
    sprite = open_image("sprites/next_button.png")
    next_screens = [
        "StartScreen",
        "IntermediateScreen",
        "ExtremeScreen",
        "RateUsScreen",
    ]
