import json
from pathlib import Path

CUR_DIR = Path(__file__).parent
SRC_DIR = CUR_DIR.parent


class Translation:
    def __init__(self, words: list[str]):
        self.words = words

    def __repr__(self):
        return f"Translation({self.words})"

    def __bool__(self):
        return bool(self.words)


class Tesaurus:
    def __init__(self, filename: str):
        self.filename = filename
        with open(SRC_DIR / self.filename, "r", encoding="utf-8") as f:
            self.dict = json.load(f)

    def save(self):
        with open(SRC_DIR / self.filename, "w", encoding="utf-8") as f:
            json.dump(self.dict, f, indent=4, ensure_ascii=False)

    def get_translation(self, rus_word) -> Translation | None:
        words = self.dict.get(rus_word)
        if words:
            return Translation(words)

        return None

    def set_translation(self, rus_word, deu_word):
        if rus_word not in self.dict:
            self.dict[rus_word] = []

        self.dict[rus_word].append(deu_word)
        self.save()


tesaurus = Tesaurus("rus-deu.json")
