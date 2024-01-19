import pytest

from helpers.utils import open_image

from screen import StartScreen
from screen._base import BaseScreen
from screen.attention import AttentionScreen
from screen.extreme import ExtremeScreen
from screen.finish import FinishScreen
from screen.intermediate import IntermediateScreen
from screen.timeout import TimeoutScreen


@pytest.mark.parametrize(
    "filename, expected_screen_cls",
    [
        ("screen/_attention.png", AttentionScreen),
        ("screen/_extreme.png", ExtremeScreen),
        ("screen/_finish.png", FinishScreen),
        ("screen/_intermediate.png", IntermediateScreen),
        ("screen/_start_12.png", StartScreen),
        ("screen/_timeout.png", TimeoutScreen),
    ],
)
def test_is_current_screen(
    filename: str, expected_screen_cls: type[BaseScreen]
) -> None:
    screenshot = open_image(filename)
    assert expected_screen_cls.is_current(screenshot) is True

    assert all(
        screen_cls.is_current(screenshot) is False
        for screen_cls in set(BaseScreen.__subclasses__()) - {expected_screen_cls}
    )
