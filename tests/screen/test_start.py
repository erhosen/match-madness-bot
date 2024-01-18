import pytest

from helpers.utils import open_image
from screen.start import StartScreen


@pytest.mark.parametrize(
    "filename, expected",
    [
        # ("screen/_start_1.png", False),
        # ("screen/_start_2.png", False),
        # ("screen/_start_3.png", False),
        # ("screen/_start_4.png", False),
        # ("screen/_start_5.png", False),
        # ("screen/_start_6.png", False),
        # ("screen/_start_7.png", False),
        # ("screen/_start_8.png", False),
        # ("screen/_start_9.png", False),
        # ("screen/_start_10.png", False),
        # ("screen/_start_11.png", False),
        ("screen/_start_12.png", True),
        ("screen/_attention.png", False),
        ("screen/_extreme.png", False),
        ("screen/_finish.png", False),
        (
            "screen/_intermediate.png",
            False,
        ),  # Unfortunatelly, this is True. TODO: Fix it
    ],
)
def test_is_current_12(filename: str, expected: bool) -> None:
    screenshot = open_image(filename)
    assert StartScreen.is_current(screenshot) == expected
