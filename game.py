from utils import display_hangman, word_update
from constants import alphabet_list




def choose() -> bool:
    while True:
        user_choice = input("Начать новую игру/Выйти (Start/Exit): ")
        if user_choice.lower() in ["start", "s", "старт"]:
            return True
        elif user_choice.lower() in ["exit", "e", "выход"]:
            return False
        else:
            print("Вы ввели неправильный ответ")



def is_valid_letter(guessed_letters: list, missed_letters: list) -> str:
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



def play(word: str):
    guessed = False
    guessed_letters = []
    missed_letters = []
    tries = 6
    mistakes = 0

    print("Добро пожаловать в игру 'Виселица'!")


    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_update(word, guessed_letters))
        print(f"Кол-во ошибок: {mistakes}")
        user_input = is_valid_letter(guessed_letters, missed_letters)

        if user_input in word:
            guessed_letters.append(user_input)
            print("Верно! Буква", user_input, "есть в слове.")
            if word_update(word, guessed_letters).count("_") == 0:
                guessed = True
                print("Поздравляем, вы угадали слово! Загаданное слово было:", word)
                break

        else:
            tries -= 1
            mistakes += 1
            missed_letters.append(user_input)
        if tries == 0:
            print(display_hangman(tries))
            print(f"Кол-во ошибок: {mistakes}")
            print("Вы проиграли! Загаданное слово было:", word)
            break