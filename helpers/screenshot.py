from functools import lru_cache
from pathlib import Path

import pyautogui
from PIL import Image
from pyscreeze import Box, Point

pyautogui.PAUSE = 0

CUR_DIR = Path(__file__).parent
PROJECT_DIR = CUR_DIR.parent
IMAGES_DIR = PROJECT_DIR / "data" / "images"


def center(box: Box) -> Point:
    center_x = int(box.left + box.width / 2)
    center_y = int(box.top + box.height / 2)
    return Point(x=center_x, y=center_y)


class Screenshot:
    def __init__(self, image: Image.Image):
        self.image = image

    def _locate_sprite(
        self, sprite: Image.Image, confidence: float = 0.9
    ) -> Point | None:
        """Find sprite on screenshot and return its central point.

        Returns None if sprite is not found.
        """
        try:
            box = pyautogui.locate(sprite, self.image, confidence=confidence)
            central_point = center(box)
            return central_point
        except pyautogui.ImageNotFoundException:
            return None

    def __contains__(self, sprite: Image.Image) -> bool:
        central_point = self._locate_sprite(sprite)
        return bool(central_point)

    def save(self, filename: str) -> None:
        self.image.save(IMAGES_DIR / filename)

    @classmethod
    def open(cls, filename: str) -> "Screenshot":
        image = Image.open(IMAGES_DIR / filename)
        return cls(image)

    @classmethod
    def take(cls) -> "Screenshot":
        menubar_height = cls.get_menubar_height()
        image = pyautogui.screenshot(region=(0, menubar_height, 1050, 786))
        return cls(image)

    @classmethod
    def click(cls, point: Point) -> None:
        """Clicks point on the screen.

        Screen agnostic.
        """
        menubar_height = cls.get_menubar_height()
        pyautogui.click(point.x, point.y + menubar_height)

    def click_on(self, sprite: Image.Image) -> None:
        """Clicks sprite on the screen.

        Screen agnostic.
        """
        central_point = self._locate_sprite(sprite)
        self.click(central_point)

    @staticmethod
    @lru_cache
    def get_menubar_height() -> int:
        screen_resolution = pyautogui.resolution()

        match screen_resolution:
            case (3440, 1440):
                menubar_height = 54
            case (1800, 1169):
                menubar_height = 73
            case _:
                raise ValueError(f"Unknown resolution: {screen_resolution}")

        return menubar_height
