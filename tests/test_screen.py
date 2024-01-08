from helpers.utils import open_image
from screen.extreme import ExtremeScreen
import pytest


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("screen/extreme.png", True),
        ("screen/start.png", False),
    ],
)
def test_extreme_screen_is_current(filename: str, expected: bool) -> None:
    screenshot = open_image(filename)
    assert ExtremeScreen.is_current(screenshot) == expected
