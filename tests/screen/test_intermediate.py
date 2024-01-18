from helpers.utils import open_image
from screen.intermediate import IntermediateScreen
import pytest


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("screen/_intermediate.png", True),
        ("screen/_attention.png", False),
        ("screen/_extreme.png", False),
        ("screen/_finish.png", False),
        ("screen/_start_12.png", False),
    ],
)
def test_is_current(filename: str, expected: bool) -> None:
    screenshot = open_image(filename)
    assert IntermediateScreen.is_current(screenshot) == expected
