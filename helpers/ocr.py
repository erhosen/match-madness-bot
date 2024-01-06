import re

import pytesseract
from PIL.Image import Image

JUST_WORDS_REGEX = re.compile(r"[^\w\s]")


def remove_punctuation(word: str) -> str:
    return JUST_WORDS_REGEX.sub("", word)


def process_image_tesseract(image: Image, lang: str) -> str:
    word = pytesseract.image_to_string(image, lang=lang, config="--psm 7")
    if word:
        word = word.strip()
        word = remove_punctuation(word)
        return word.lower()
    else:
        # image.save(f"image_{lang}.png")
        print("Can't recognize word, suppose it's И")
        return "и"


def get_number_from_image(image: Image) -> int | None:
    try:
        number = pytesseract.image_to_string(
            image, config="--psm 7 -c tessedit_char_whitelist=01234567899"
        )
        return int(number)
    except ValueError:
        return None
