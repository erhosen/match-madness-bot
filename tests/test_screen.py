import pytest

from helpers.screenshot import Screenshot
from screen import StartScreen
from screen._base import BaseScreen
from screen.attention import AttentionScreen
from screen.double_points import DoublePointsScreen
from screen.extreme import ExtremeScreen
from screen.finish import FinishScreen
from screen.game import GameScreen
from screen.intermediate import IntermediateScreen
from screen.rate_us import RateUsScreen
from screen.timeout import TimeoutScreen
from screen.wait_where_are_you import WaitWhereAreYouScreen


@pytest.mark.parametrize(
    "filename, expected_screen_cls",
    [
        ("screen/_attention_1.png", AttentionScreen),
        ("screen/_attention_2.png", AttentionScreen),
        ("screen/_attention_3.png", AttentionScreen),
        ("screen/_extreme.png", ExtremeScreen),
        ("screen/_finish.png", FinishScreen),
        ("screen/_game.png", GameScreen),
        ("screen/_intermediate_1.png", IntermediateScreen),
        ("screen/_intermediate_2.png", IntermediateScreen),
        ("screen/_intermediate_3.png", IntermediateScreen),
        ("screen/_intermediate_4.png", IntermediateScreen),
        ("screen/_rate_us.png", RateUsScreen),
        ("screen/_start_1.png", StartScreen),
        ("screen/_start_12.png", StartScreen),
        ("screen/_timeout.png", TimeoutScreen),
        ("screen/_wait_where_are_you.png", WaitWhereAreYouScreen),
        ("screen/_double_points.png", DoublePointsScreen),
    ],
)
def test_is_current_screen(
    filename: str, expected_screen_cls: type[BaseScreen]
) -> None:
    screenshot = Screenshot.open(filename)

    assert expected_screen_cls.is_current(screenshot) is True
    # for screen_cls in set(BaseScreen.__subclasses__()) - {expected_screen_cls}:
    #     assert screen_cls.is_current(screenshot) is False, screen_cls


@pytest.mark.parametrize(
    "filename, expected_lvl",
    [
        ("screen/_start_1.png", 1),
        ("screen/_start_2.png", 2),
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
    screenshot = Screenshot.open(filename)
    assert StartScreen.determine_lvl(screenshot) == expected_lvl


@pytest.mark.parametrize(
    "screen,filename,expected_next_screen",
    [
        (WaitWhereAreYouScreen, "screen/_start_1.png", StartScreen),
        (WaitWhereAreYouScreen, "screen/_finish.png", FinishScreen),
        (TimeoutScreen, "screen/_start_1.png", StartScreen),
        (TimeoutScreen, "screen/_wait_where_are_you.png", WaitWhereAreYouScreen),
        (StartScreen, "screen/_attention_1.png", AttentionScreen),
        (StartScreen, "screen/_double_points.png", DoublePointsScreen),
        (RateUsScreen, "screen/_start_1.png", StartScreen),
        (RateUsScreen, "screen/_intermediate_1.png", IntermediateScreen),
        (RateUsScreen, "screen/_extreme.png", ExtremeScreen),
        (IntermediateScreen, "screen/_start_1.png", StartScreen),
        (IntermediateScreen, "screen/_intermediate_1.png", IntermediateScreen),
        (IntermediateScreen, "screen/_extreme.png", ExtremeScreen),
        (GameScreen, "screen/_attention_1.png", AttentionScreen),
        (GameScreen, "screen/_timeout.png", TimeoutScreen),
        (GameScreen, "screen/_wait_where_are_you.png", WaitWhereAreYouScreen),
        (FinishScreen, "screen/_start_12.png", StartScreen),
        (FinishScreen, "screen/_intermediate_1.png", IntermediateScreen),
        (FinishScreen, "screen/_extreme.png", ExtremeScreen),
        # (FinishScreen, "screen/_rate_us.png", RateUsScreen),  # Collision with ExtremeScreen
        (ExtremeScreen, "screen/_start_1.png", StartScreen),
        (DoublePointsScreen, "screen/_attention_1.png", AttentionScreen),
        (AttentionScreen, "screen/_finish.png", FinishScreen),
        (AttentionScreen, "screen/_wait_where_are_you.png", WaitWhereAreYouScreen),
        # (AttentionScreen, "screen/_game.png", GameScreen),  # Done manually for now
    ],
)
def test_determine_next_screen(
    screen: type[BaseScreen], filename: str, expected_next_screen: type[BaseScreen]
) -> None:
    assert (
        screen.determine_next_screen(
            screenshot_fn=lambda: Screenshot.open(filename),
            sleep_fn=lambda _: None,
        )
        == expected_next_screen
    )
