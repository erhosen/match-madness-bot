from helpers.constants import Language
from helpers.match_madness import MatchMadness
from helpers.screenshot import Screenshot


def test_get_images():
    match_madness = MatchMadness(lang_left=Language.RUS, lang_right=Language.DEU)
    screenshot = Screenshot.open("screen/_game.png")
    left_images, right_images = match_madness.get_images(screenshot)
    assert len(left_images) == 5
    assert len(right_images) == 5
