import pytest

from helpers.utils import open_image
from screen.attention import AttentionScreen


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("screen/_attention.png", True),
        ("screen/_extreme.png", False),
        ("screen/_start.png", False),
    ],
)
def test_attention(filename: str, expected: bool) -> None:
    screenshot = open_image(filename)
    assert AttentionScreen.is_current(screenshot) == expected
