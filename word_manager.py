import random as r
from pathlib import Path
from constants import rus_letters


BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "gamewords.txt"


def get_word() -> None | str:
    try:
        with open (file_path, encoding="utf-8") as f:
            words = f.read().split()
            if not words:
                print("Файл оказался пустым(")
                return None

            valid_words = []

            for word in words:
                word = word.upper()
                if len(word) > 4 and all(letter in rus_letters for letter in word):
                    valid_words.append(word)

            if not valid_words:
                print("Нет подходящих слов написанных кириллицей")
                return None

            return r.choice(valid_words)

    except FileNotFoundError:
        print("Файл не найден")
        return None
