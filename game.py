from utils import display_hangman, word_update
from constants import alphabet_list, tries




def choose() -> bool:
    while True:
        user_choice = input("Начать новую игру/Выйти (Start/Exit): ")
        if user_choice.lower() in ["start", "s", "старт"]:
            return True
        elif user_choice.lower() in ["exit", "e", "выход"]:
            return False
        else:
            print("Вы ввели неправильный ответ")



def valid_letter(guessed_letters: list, missed_letters: set) -> str:
    while True:
        user_input = input("Введите кириллическую букву: ").upper()

        if user_input not in alphabet_list:
            print("Вы ввели не кириллическую букву!")
        elif user_input in guessed_letters:
            print("Вы уже называли эту букву!")
        elif user_input in missed_letters:
            print("Этой буквы нету в слове, вы ее уже называли")
        else:
            return user_input



def play(word: str) -> None:
    guessed_letters = []
    missed_letters = set()

    print("Добро пожаловать в игру 'Виселица'!")


    while len(missed_letters) < 6:
        print(display_hangman(len(missed_letters)))
        print(word_update(word, guessed_letters))
        print(f"Кол-во ошибок: {len(missed_letters)}")
        user_input = valid_letter(guessed_letters, missed_letters)

        if user_input in word:
            guessed_letters.append(user_input)
            print("Верно! Буква", user_input, "есть в слове.")
            if word_update(word, guessed_letters).count("_") == 0:
                print(word)
                print("Поздравляем, вы угадали слово! Загаданное слово было:", word)
                break

        else:
            missed_letters.add(user_input)

    print(display_hangman(len(missed_letters)))
    print(f"Кол-во ошибок: {len(missed_letters)}")
    print("Вы проиграли! Загаданное слово было:", word)
