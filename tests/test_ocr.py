import pytest

from helpers.constants import LANG_DEU, LANG_RUS, Language
from helpers.ocr import _process_image_tesseract, recognize_word, recognize_number
from helpers.utils import open_image


def test_ihr():
    image = open_image("words/ihr.png")
    word = _process_image_tesseract(image, LANG_DEU)
    assert word == "ihr"


def test_oni():
    image = open_image("words/oni.png")
    # increase contrast
    image = image.point(lambda x: x * 1.5)
    word = _process_image_tesseract(image, LANG_RUS)
    assert word == "они"


def test_nie():
    image = open_image("words/nie.png")
    # inverse image colors
    image = image.point(lambda x: 255 - x)
    word = _process_image_tesseract(image, LANG_DEU)
    assert word == "nie"


@pytest.mark.parametrize(
    "filename, lang, expected_word",
    [
        ("words/_left_0.png", Language.RUS, "но"),
        ("words/_left_1.png", Language.RUS, "удобный"),
        ("words/_left_2.png", Language.RUS, "много"),
        ("words/_left_3.png", Language.RUS, "плохо"),
        ("words/_left_4.png", Language.RUS, "тринадцать"),
        ("words/_right_0.png", Language.DEU, "bequem"),
        ("words/_right_1.png", Language.DEU, "schlecht"),
        ("words/_right_2.png", Language.DEU, "aber"),
        ("words/_right_3.png", Language.DEU, "dreizehn"),
        ("words/_right_4.png", Language.DEU, "viel"),
    ],
)
def test_word_recognition(filename: str, lang: Language, expected_word: str):
    image = open_image(filename)
    word = recognize_word(image, lang)
    assert word == expected_word


def test_number_recognition():
    image = open_image("checkbox/lvl8.png")
    number = recognize_number(image)
    assert number == 12
