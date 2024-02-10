from abc import ABC, abstractmethod

from helpers.screenshot import Screenshot


class BaseScreen(ABC):
    def __init__(self):
        print(f"Current screen: {self.__class__.__name__}")

    @classmethod
    @abstractmethod
    def is_current(cls, screenshot: Screenshot) -> bool:
        pass

    @classmethod
    @abstractmethod
    def determine_next_screen(cls) -> type["BaseScreen"]:
        pass

    @abstractmethod
    def next(self) -> "BaseScreen":
        pass
