import pytest

from helpers.utils import open_image
from screen import StartScreen
from screen._base import BaseScreen
from screen.attention import AttentionScreen
from screen.extreme import ExtremeScreen
from screen.finish import FinishScreen
from screen.game import GameScreen
from screen.intermediate import IntermediateScreen
from screen.timeout import TimeoutScreen
from screen.wait_where_are_you import WaitWhereAreYouScreen


@pytest.mark.parametrize(
    "filename, expected_screen_cls",
    [
        ("screen/_attention.png", AttentionScreen),
        ("screen/_attention_2.png", AttentionScreen),
        ("screen/_extreme.png", ExtremeScreen),
        ("screen/_finish.png", FinishScreen),
        ("screen/_intermediate.png", IntermediateScreen),
        ("screen/_start_12.png", StartScreen),
        ("screen/_timeout.png", TimeoutScreen),
        ("screen/_game.png", GameScreen),
        ("screen/_wait_where_are_you.png", WaitWhereAreYouScreen),
    ],
)
def test_is_current_screen(
    filename: str, expected_screen_cls: type[BaseScreen]
) -> None:
    # Make sure that the screenshot belongs to the expected screen, and not to any other screen
    screenshot = open_image(filename)

    assert expected_screen_cls.is_current(screenshot) is True
    for screen_cls in set(BaseScreen.__subclasses__()) - {expected_screen_cls}:
        assert screen_cls.is_current(screenshot) is False, screen_cls
