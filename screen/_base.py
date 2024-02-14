import time
from abc import ABC
from typing import Callable

from helpers.screenshot import Screenshot, Sprite


class BaseScreen(ABC):
    look_for_sprite: Sprite | None = None
    click_on_sprite: Sprite | None = None
    next_screens: list[str] = []

    def __init__(self):
        print(f"Current screen: {self.__class__.__name__}")

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        if cls.look_for_sprite is None:
            raise NotImplementedError(
                "You must define a look_for_sprite for the screen, or override this method"
            )

        return screenshot.has_sprite(cls.look_for_sprite)

    @classmethod
    def determine_next_screen(
        cls, screenshot_fn: Callable = Screenshot.take, sleep_fn: Callable = time.sleep
    ) -> type["BaseScreen"]:
        if not cls.next_screens:
            raise NotImplementedError(
                "You must define next_screens for the screen, or override this method"
            )

        next_screen_classes = [
            sub_cls
            for sub_cls in BaseScreen.__subclasses__()
            if sub_cls.__name__ in cls.next_screens
        ]
        for _ in range(30):
            sleep_fn(1)

            screenshot = screenshot_fn()
            for screen_cls in next_screen_classes:
                if screen_cls.is_current(screenshot):
                    return screen_cls

        raise ValueError("Can't determine next screen")

    @classmethod
    def next(cls) -> "BaseScreen":
        if cls.click_on_sprite is None:
            raise NotImplementedError(
                "You must define a click_on_sprite for the screen, or override this method"
            )

        Screenshot.take().click_on(cls.click_on_sprite.image)
        NextScreen = cls.determine_next_screen()  # noqa

        return NextScreen()
