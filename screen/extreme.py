from helpers.utils import open_image
from screen._base import BaseScreen


class ExtremeScreen(BaseScreen):
    sprite = open_image("sprites/start_button.png")
    next_screens = [
        "StartScreen",
    ]
