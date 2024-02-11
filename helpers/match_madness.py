import time

from PIL.Image import Image
from pyscreeze import Point

from helpers.constants import Language, TILE_WIDTH, TILE_HEIGHT, DISTANCE_BETWEEN_TILES
from helpers.ocr import recognize_word
from helpers.screenshot import Screenshot
from helpers.tesaurus import Translation, Tesaurus
from helpers.utils import (
    TimeoutExpired,
    input_with_timeout,
)


class NoTranslationFound(Exception):
    pass


class VirtualKeyboard:
    Y0 = 266
    Y_SHIFT = 70

    def __init__(self, lang: Language, x_shift: int):
        self.lang = lang
        self.x_shift = x_shift

        self.idx_to_reload: list[int | None] = [None, None, None]
        self.words: dict[int, str | None] = {}
        self.images: dict[int, Image | None] = {}

    def load(self, images: list[Image]):
        for image_idx in range(5):
            image = images[image_idx]
            word = recognize_word(image, self.lang)
            self.words[image_idx] = word
            self.images[image_idx] = image

    def reload(self, images: list[Image]):
        image_idx = self.idx_to_reload.pop(0)
        if image_idx is None:
            # First few iterations, we don't need to reload anything
            # But we need to sleep about the same time as it takes to reload
            time.sleep(0.1)
            return

        image = images[image_idx]
        word = recognize_word(image, self.lang)
        self.words[image_idx] = word
        self.images[image_idx] = image

    def get_idx(self, word: str) -> int:
        for idx, word_ in self.words.items():
            if word_ == word:
                return idx
        raise ValueError(f"Word [{word}] not found in words: {self.words}")

    def get_translation_idx(self, translation: Translation) -> int | None:
        # we iterate over translations, because the priority matters. Example: "там" -> ["da", "dort"]
        for translation_word in translation.words:
            try:
                return self.get_idx(translation_word)
            except ValueError:
                continue

        return None

    def get_word(self, idx: int) -> str:
        word = self.words[idx]
        assert word is not None, f"Word with idx {idx} is None!"
        return word

    def click_on_idx(self, idx: int) -> None:
        point = Point(self.x_shift, self.Y0 + idx * self.Y_SHIFT)
        Screenshot.click(point)

        self.words[idx] = None
        self.images[idx] = None
        self.idx_to_reload.append(idx)

    def print(self):
        for idx, word in self.words.items():
            print(idx, word if word else "")


class MatchMadness:
    LEFT_X_SHIFT = 365
    RIGHT_X_SHIFT = 690

    def __init__(self, lang_left: Language, lang_right: Language):
        self.lang_left = lang_left
        self.lang_right = lang_right

        self.left_keyboard = VirtualKeyboard(lang_left, self.LEFT_X_SHIFT)
        self.right_keyboard = VirtualKeyboard(lang_right, self.RIGHT_X_SHIFT)
        self.tesaurus = Tesaurus(f"{lang_left.value}-{lang_right.value}.json")

    @staticmethod
    def get_images(screenshot: Screenshot):
        x0_left = 290
        x1_left = x0_left + TILE_WIDTH
        x0_right = 615
        x1_right = x0_right + TILE_WIDTH
        y0 = 256
        y1 = y0 + TILE_HEIGHT

        left_images, right_images = [], []
        for i in range(5):
            y0_i = y0 + i * DISTANCE_BETWEEN_TILES
            y1_i = y1 + i * DISTANCE_BETWEEN_TILES
            left_image = screenshot.crop((x0_left, y0_i, x1_left, y1_i))
            right_image = screenshot.crop((x0_right, y0_i, x1_right, y1_i))
            left_images.append(left_image)
            right_images.append(right_image)

        return [left_images, right_images]

    def load(self):
        screenshot = Screenshot.take()
        left_images, right_images = self.get_images(screenshot)
        self.left_keyboard.load(left_images)
        self.right_keyboard.load(right_images)

    def process_word(self, left_word: str) -> int:
        translation = self.tesaurus.get_translation(left_word)
        if (
            translation
            and (right_index := self.right_keyboard.get_translation_idx(translation))
            is not None
        ):
            # print(f"Found translation for [{left_word}]: {translation}")
            pass
        else:
            print(f"\nNo translation found for [{left_word}]")
            self.right_keyboard.print()
            self.left_keyboard.print()
            timeout = 10
            prompt = f"Please enter translation index (timeout {timeout} sec): "
            try:
                right_index_raw = input_with_timeout(prompt, timeout)
            except TimeoutExpired as exc:
                print("Timeout expired, exiting...")
                raise NoTranslationFound(
                    f"Can't find translation for [{left_word}]"
                ) from exc
            else:
                right_index = int(right_index_raw)
                right_word = self.right_keyboard.get_word(right_index)
                self.tesaurus.set_translation(left_word, right_word)

        return right_index

    def process_chapter(self, iterations: int):
        self.load()

        for i in range(iterations):
            for left_idx in range(5):
                left_word = self.left_keyboard.get_word(left_idx)
                if not left_word:
                    continue

                self.left_keyboard.click_on_idx(left_idx)
                right_idx = self.process_word(left_word)
                self.right_keyboard.click_on_idx(right_idx)

                is_last_iteration = (i == iterations - 1) and (left_idx == 4)
                if is_last_iteration:
                    return

                screenshot = Screenshot.take()
                left_images, right_images = self.get_images(screenshot)
                self.left_keyboard.reload(left_images)
                self.right_keyboard.reload(right_images)
