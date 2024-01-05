import re

import pytesseract
from PIL.Image import Image

JUST_WORDS_REGEX = re.compile(r"[^\w\s]")


def process_image_tesseract(image: Image, lang: str) -> str:
    word = pytesseract.image_to_string(image, lang=lang, config="--psm 7")
    if word:
        word = word.strip()
        word = JUST_WORDS_REGEX.sub("", word)  # remove punctuation
        return word.lower()
    else:
        # image.save(f"image_{lang}.png")
        print("Can't recognize word, suppose it's И")
        return "и"
