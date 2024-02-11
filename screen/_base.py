import time
from abc import ABC, abstractmethod
from typing import Callable

from helpers.screenshot import Screenshot


class BaseScreen(ABC):
    sprite = None
    next_screens: list[str] = []

    def __init__(self):
        print(f"Current screen: {self.__class__.__name__}")

    @classmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        if cls.sprite is None:
            raise NotImplementedError(
                "You must define a sprite for this screen, or override this method"
            )

        return cls.sprite in screenshot

    @classmethod
    def determine_next_screen(
        cls, screenshot_fn: Callable = Screenshot.take, sleep_fn: Callable = time.sleep
    ) -> type["BaseScreen"]:
        if not cls.next_screens:
            raise NotImplementedError(
                "You must define next_screens for this screen, or override this method"
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

    @abstractmethod
    def next(self) -> "BaseScreen":
        pass
