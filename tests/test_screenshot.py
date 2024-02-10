from unittest.mock import patch

import pytest

from helpers.screenshot import Screenshot


def test_get_menubar_height() -> None:
    with patch("helpers.screenshot.pyautogui.resolution", return_value=(3440, 1440)):
        assert Screenshot.get_menubar_height() == 54

    # same value returned from cache
    assert Screenshot.get_menubar_height() == 54

    Screenshot.get_menubar_height.cache_clear()  # type: ignore

    with patch("helpers.screenshot.pyautogui.resolution", return_value=(1800, 1169)):
        assert Screenshot.get_menubar_height() == 73

    # same value returned from cache
    assert Screenshot.get_menubar_height() == 73

    Screenshot.get_menubar_height.cache_clear()  # type: ignore

    with patch("helpers.screenshot.pyautogui.resolution", return_value=(999, 999)):
        with pytest.raises(ValueError):
            Screenshot.get_menubar_height()
