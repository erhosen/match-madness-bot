import time
from functools import partial

from PIL.Image import Image

from helpers.constants import (
    LANG_RUS,
    LANG_DEU,
    LEVELS_CONFIG,
    TILE_WIDTH,
    TILE_HEIGHT,
    DISTANCE_BETWEEN_TILES,
)
from helpers.ocr import process_image_tesseract
from screen._base import BaseScreen
from helpers.tesaurus import Translation, tesaurus
from helpers.utils import (
    input_with_timeout,
    TimeoutExpired,
    take_screenshot,
    click,
    save_image,
    pixel_matches_color,
)


class NoTranslationFound(Exception):
    pass


class VirtualKeyboard:
    X_SHIFT = {
        "rus": 365,
        "deu": 690,
    }
    Y0 = 266
    Y_SHIFT = 70

    def __init__(self, lang: str):
        self.lang = lang

        self.idx_to_reload: list[int | None] = [None, None, None]
        self.words: dict[int, str | None] = {}
        self.images: dict[int, Image | None] = {}

    def load(self, images: list[Image]):
        for image_idx in range(5):
            image = images[image_idx]
            word = process_image_tesseract(image, self.lang)
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
        word = process_image_tesseract(image, self.lang)
        self.words[image_idx] = word
        self.images[image_idx] = image

    def get_idx(self, word: str) -> int:
        for idx, word_ in self.words.items():
            if word_ == word:
                return idx
        raise ValueError(f"Word [{word}] not found in words: {self.words}")

    def get_translation_idx(self, translation: Translation) -> int | None:
        # we iterate over translations, because the priority matters. Example: "a" -> ["sondern", "wie"]
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

    @property
    def x_shift(self) -> int:
        return self.X_SHIFT[self.lang]

    def click_on_idx(self, idx: int) -> None:
        click(self.x_shift, self.Y0 + idx * self.Y_SHIFT)

        self.words[idx] = None
        self.images[idx] = None
        self.idx_to_reload.append(idx)

    def print(self):
        for idx, word in self.words.items():
            print(idx, word if word else "")
        for idx, image in self.images.items():
            if image:
                save_image(image, f"words/{self.lang}_{idx}.png")


class GameScreen(BaseScreen):
    def __init__(self, lvl: int, chapter: int):
        self.lvl = lvl
        self.chapter = chapter

        self.rus_keyboard = VirtualKeyboard(LANG_RUS)
        self.deu_keyboard = VirtualKeyboard(LANG_DEU)
        super().__init__()

    def process_word(self, rus_word: str) -> int:
        translation = tesaurus.get_translation(rus_word)
        if (
            translation
            and (deu_index := self.deu_keyboard.get_translation_idx(translation))
            is not None
        ):
            # print(f"Found translation for [{rus_word}]: {translation}")
            pass
        else:
            print(f"\nNo translation found for [{rus_word}]")
            self.deu_keyboard.print()
            self.rus_keyboard.print()
            timeout = 10
            prompt = f"Please enter translation index (timeout {timeout} sec): "
            try:
                deu_index_raw = input_with_timeout(prompt, timeout)
            except TimeoutExpired as exc:
                print("Timeout expired, exiting...")
                raise NoTranslationFound(
                    f"Can't find translation for [{rus_word}]"
                ) from exc
            else:
                deu_index = int(deu_index_raw)
                deu_word = self.deu_keyboard.get_word(deu_index)
                tesaurus.set_translation(rus_word, deu_word)

        return deu_index

    def process_chapter(self):
        rus_images, deu_images = self.get_images()
        self.rus_keyboard.load(rus_images)
        self.deu_keyboard.load(deu_images)

        iterations = LEVELS_CONFIG[self.lvl][self.chapter]
        for i in range(iterations):
            for rus_idx in range(5):
                rus_word = self.rus_keyboard.get_word(rus_idx)
                if not rus_word:
                    continue

                self.rus_keyboard.click_on_idx(rus_idx)
                deu_idx = self.process_word(rus_word)
                self.deu_keyboard.click_on_idx(deu_idx)

                is_last_iteration = (i == iterations - 1) and (rus_idx == 4)
                if is_last_iteration:
                    return

                rus_images, deu_images = self.get_images()
                self.rus_keyboard.reload(rus_images)
                self.deu_keyboard.reload(deu_images)

    def get_images(self):
        screenshot = take_screenshot()
        # Grayscale
        screenshot = screenshot.convert("L")
        # Invert colors && increase contrast
        screenshot = screenshot.point(lambda x: (255 - x) * 1.5)

        x0_left = 290
        x1_left = x0_left + TILE_WIDTH
        x0_right = 615
        x1_right = x0_right + TILE_WIDTH
        y0 = 256
        y1 = y0 + TILE_HEIGHT

        rus_images, deu_images = [], []
        for i in range(5):
            y0_i = y0 + i * DISTANCE_BETWEEN_TILES
            y1_i = y1 + i * DISTANCE_BETWEEN_TILES
            rus_image = screenshot.crop((x0_left, y0_i, x1_left, y1_i))
            deu_image = screenshot.crop((x0_right, y0_i, x1_right, y1_i))
            rus_images.append(rus_image)
            deu_images.append(deu_image)

        return [rus_images, deu_images]

    EXIT_BUTTON = (115, 28)
    PRESS_PAIRS_TEXT = (221, 145)
    DUOLINGO_WHITE = (255, 255, 255)
    DUOLINGO_GRAY = (88, 102, 110)

    @classmethod
    def is_current(cls, screenshot: Image) -> bool:
        return pixel_matches_color(
            cls.PRESS_PAIRS_TEXT, cls.DUOLINGO_WHITE, image=screenshot
        ) and pixel_matches_color(cls.EXIT_BUTTON, cls.DUOLINGO_GRAY, image=screenshot)

    def determine_next_screen(self) -> type[BaseScreen] | partial[BaseScreen]:
        from screen.attention import AttentionScreen
        from screen.timeout import TimeoutScreen
        from screen.wait_where_are_you import WaitWhereAreYouScreen

        for _ in range(20):
            time.sleep(1)
            screenshot = take_screenshot()

            if AttentionScreen.is_current(screenshot):
                # return partial because we need to pass lvl and chapter
                return partial(AttentionScreen, lvl=self.lvl, chapter=self.chapter)
            elif TimeoutScreen.is_current(screenshot):
                return TimeoutScreen
            elif WaitWhereAreYouScreen.is_current(screenshot):
                return WaitWhereAreYouScreen

        raise ValueError("Can't determine next screen")

    def next(self):
        try:
            self.process_chapter()
        except NoTranslationFound:
            print("No translation found, trying to continue...")

        NextScreen = self.determine_next_screen()
        return NextScreen()


if __name__ == "__main__":
    screen = GameScreen(lvl=1, chapter=1)
    _screenshot = take_screenshot()
    save_image(_screenshot, "screen/game.png")
    is_current = screen.is_current(_screenshot)
    print(is_current)
