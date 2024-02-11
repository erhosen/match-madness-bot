from helpers.utils import open_image
from screen._base import BaseScreen


class WaitWhereAreYouScreen(BaseScreen):
    sprite = open_image("sprites/exit_button.png")
    next_screens = ["StartScreen", "FinishScreen"]
