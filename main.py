from game import play, choose
from word_manager import get_word


def main() -> None:
    while True:
        if choose():
            word = get_word()
            if word is not None:
                play(word)
        else:
            print("До свидания!")
            break


if __name__ == "__main__":
    main()
