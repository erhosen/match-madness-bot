import select
import sys
import time
from functools import wraps

import pyautogui
from PIL import Image
from pathlib import Path

from pyscreeze import Box, Point

pyautogui.PAUSE = 0

CUR_DIR = Path(__file__).parent
PROJECT_DIR = CUR_DIR.parent
IMAGES_DIR = PROJECT_DIR / "data" / "images"


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
        MENUBAR_HEIGHT = 54
    case (1800, 1169):
        MENUBAR_HEIGHT = 73
    case _:
        raise ValueError(f"Unknown resolution: {SCREEN_RESOLUTION}")

DUOLINGO_WINDOW = (0, MENUBAR_HEIGHT, 1050, 786)


def take_screenshot() -> Image.Image:
    screenshot = pyautogui.screenshot(region=DUOLINGO_WINDOW)
    # assert screenshot.size == (1050, 786)
    return screenshot


def click(x: int, y: int) -> None:
    """Click on x, y coordinates.

    Screen agnostic.
    """
    pyautogui.click(x, y + MENUBAR_HEIGHT)


def click_on(sprite: Image.Image) -> None:
    """Click on sprite.

    Screen agnostic.
    """
    point = _locate_sprite(sprite, take_screenshot())
    click(point.x, point.y)


def get_image_pixel(image: Image.Image, x: int, y: int) -> tuple[int, int, int]:
    _pixel = image.getpixel((x, y))
    return _pixel[0], _pixel[1], _pixel[2]


def get_pixel(x: int, y: int) -> tuple[int, int, int]:
    """Get pixel color on x, y coordinates.

    Screen agnostic.
    """
    screenshot = take_screenshot()
    # save_screenshot(screenshot, "screen.png")
    pixel = screenshot.getpixel((x, y))
    return pixel[0], pixel[1], pixel[2]


def save_image(image: Image.Image, name: str) -> None:
    image.save(IMAGES_DIR / name)


def open_image(name: str) -> Image.Image:
    return Image.open(IMAGES_DIR / name)


def pixel_matches_color(
    pixel: tuple[int, int],
    color: tuple[int, int, int],
    threshold: int = 10,
    image: Image.Image = None,
) -> bool:
    x, y = pixel
    if image:
        image_pixel = get_image_pixel(image, x, y)
    else:
        image_pixel = get_pixel(x, y)

    # print(f"image_pixel: {image_pixel}, color: {color}")
    return all(abs(image_pixel[i] - color[i]) < threshold for i in range(3))


def center(box: Box) -> Point:
    center_x = int(box.left + box.width / 2)
    center_y = int(box.top + box.height / 2)
    return Point(x=center_x, y=center_y)


def _locate_sprite(
    sprite: Image.Image, screenshot: Image.Image, confidence: float = 0.9
) -> Point | None:
    """Find sprite on screenshot and return its central point.

    Returns None if sprite is not found.
    """
    try:
        box = pyautogui.locate(sprite, screenshot, confidence=confidence)
        central_point = center(box)
        return central_point
    except pyautogui.ImageNotFoundException:
        return None


def has_sprite(
    sprite: Image.Image, screenshot: Image.Image, confidence: float = 0.9
) -> bool:
    """Check if sprite is present on screenshot.

    Returns True if sprite is found, False otherwise.
    """
    central_point = _locate_sprite(sprite, screenshot, confidence=confidence)
    return bool(central_point)
