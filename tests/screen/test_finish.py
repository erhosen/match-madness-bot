from helpers.utils import open_image
from screen.finish import FinishScreen
import pytest


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("screen/_finish.png", True),
        ("screen/_attention.png", False),
        ("screen/_extreme.png", False),
        ("screen/_intermediate.png", False),
        ("screen/_start_12.png", False),
    ],
)
def test_is_current(filename: str, expected: bool) -> None:
    screenshot = open_image(filename)
    assert FinishScreen.is_current(screenshot) == expected
