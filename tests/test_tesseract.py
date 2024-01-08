from helpers.constants import LANG_DEU, LANG_RUS
from helpers.ocr import process_image_tesseract
from helpers.utils import open_image


def test_ihr():
    image = open_image("words/ihr.png")
    word = process_image_tesseract(image, LANG_DEU)
    assert word == "ihr"


def test_oni():
    image = open_image("words/oni.png")
    # increase contrast
    image = image.point(lambda x: x * 1.5)
    word = process_image_tesseract(image, LANG_RUS)
    assert word == "они"


def test_nie():
    image = open_image("words/nie.png")
    # inverse image colors
    image = image.point(lambda x: 255 - x)
    word = process_image_tesseract(image, LANG_DEU)
    assert word == "nie"
