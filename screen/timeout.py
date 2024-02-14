from helpers.screenshot import Sprite
from screen._base import BaseScreen


class TimeoutScreen(BaseScreen):
    look_for_sprite = Sprite.open("no_thanks_button.png")
    click_on_sprite = Sprite.open("no_thanks_button.png")
    next_screens = ["StartScreen", "WaitWhereAreYouScreen"]
