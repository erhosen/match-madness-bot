import select
import sys
import time
from functools import wraps

import pyautogui
from PIL.Image import Image


class TimeoutExpired(Exception):
    pass


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))
        return result

    return wrap


def input_with_timeout(prompt, timeout):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().rstrip("\n")  # expect stdin to be line-buffered

    raise TimeoutExpired


SCREEN_RESOLUTION = pyautogui.resolution()
match SCREEN_RESOLUTION:
    case (3440, 1440):
        DUOLINGO_WINDOW = (0, 54, 1050, 786)
    case (1800, 1169):
        DUOLINGO_WINDOW = (0, 73, 1050, 786)
    case _:
        raise ValueError(f"Unknown resolution: {SCREEN_RESOLUTION}")


def take_screenshot() -> Image:
    screenshot = pyautogui.screenshot(region=DUOLINGO_WINDOW)
    # assert screenshot.size == (1050, 786)
    return screenshot
