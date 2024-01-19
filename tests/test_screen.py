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
        ("screen/_attention_3.png", AttentionScreen),
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


@pytest.mark.parametrize(
    "filename, expected_lvl",
    [
        ("screen/_start_1.png", 1),
        # ("screen/_start_2.png", 2),
        ("screen/_start_3.png", 3),
        ("screen/_start_4.png", 4),
        ("screen/_start_5.png", 5),
        ("screen/_start_6.png", 6),
        ("screen/_start_7.png", 7),
        ("screen/_start_8.png", 8),
        ("screen/_start_9.png", 9),
        ("screen/_start_10.png", 10),
        ("screen/_start_11.png", 11),
        ("screen/_start_12.png", 12),
    ],
)
def test_start_screen_determine_lvl(filename: str, expected_lvl: int) -> None:
    screenshot = open_image(filename)
    assert StartScreen.determine_lvl(screenshot) == expected_lvl
