from helpers.constants import Language
from helpers.match_madness import MatchMadness
from helpers.utils import open_image, save_image


def test_get_images():
    match_madness = MatchMadness(lang_left=Language.RUS, lang_right=Language.DEU)
    screenshot = open_image("screen/_game.png")
    left_images, right_images = match_madness.get_images(screenshot)
    assert len(left_images) == 5
    assert len(right_images) == 5

    for i in range(5):
        left_image = left_images[i]
        right_image = right_images[i]

        save_image(left_image, f"words/_left_{i}.png")
        save_image(right_image, f"words/_right_{i}.png")
