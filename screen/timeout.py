from helpers.utils import open_image
from screen._base import BaseScreen


class TimeoutScreen(BaseScreen):
    sprite = open_image("sprites/no_thanks_button.png")
    next_screens = ["StartScreen", "WaitWhereAreYouScreen"]
