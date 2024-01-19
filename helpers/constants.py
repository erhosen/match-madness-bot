from enum import Enum

TILE_HEIGHT = 20
TILE_WIDTH = 150
DISTANCE_BETWEEN_TILES = 68

LANG_RUS = "rus"
LANG_DEU = "deu"


class Language(str, Enum):
    RUS = "rus"
    DEU = "deu"


LEVELS_CONFIG = {
    1: [2, 4, 6],
    2: [3, 4, 7],
    3: [3, 5, 8],
    4: [4, 6, 8],
    5: [4, 7, 9],
    6: [5, 7, 10],
    7: [6, 8, 10],
    8: [8, 9, 11],
    9: [8, 9, 12],
    10: [8, 10, 12],
    11: [9, 10, 12],
    12: [9, 10, 13],
}
