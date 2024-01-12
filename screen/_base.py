from abc import ABC, abstractmethod

from PIL.Image import Image


class BaseScreen(ABC):
    def __init__(self):
        print(f"Current screen: {self.__class__.__name__}")

    @abstractmethod
    def is_current(self, screenshot: Image):
        pass

    @abstractmethod
    def next(self) -> "BaseScreen":
        pass
