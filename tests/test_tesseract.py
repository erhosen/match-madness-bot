from PIL import Image

from helpers.constants import LANG_DEU, LANG_RUS
from helpers.ocr import process_image_tesseract


def test_ihr():
    image = Image.open("images/words/ihr.png")
    word = process_image_tesseract(image, LANG_DEU)
    assert word == "ihr"


def test_oni():
    image = Image.open("images/words/oni.png")
    # increase contrast
    image = image.point(lambda x: x * 1.5)
    image.save("../images/words/oni_contrast.png")
    word = process_image_tesseract(image, LANG_RUS)
    assert word == "они"


def test_nie():
    image = Image.open("images/words/nie.png")
    # inverse image colors
    image = image.point(lambda x: 255 - x)
    image.save("../images/words/nie_inverse.png")
    word = process_image_tesseract(image, LANG_DEU)
    assert word == "nie"
