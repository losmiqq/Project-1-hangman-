import random as r
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "gamewords.txt" 

alphabet_list = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", 
                 "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", 
                 "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"
                 ]

rus_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


# Запрос юзера продолжить/закончить игру
def choose() -> bool:
    while True:
        user_choice = input("Начать новую игру/Выйти (Start/Exit): ")
        if user_choice.lower() in ["start", "s", "старт"]:
            return True
        elif user_choice.lower() in ["exit", "e", "выход"]:
            return False
        else:
            print("Вы ввели неправильный ответ")





# Выбор случайного слова с файла
def get_word() -> str:
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


# Функция получения текущего состояния
def display_hangman(tries: int) -> str:
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


# Состояние загаданного слова
def word_update(word: str, guessed_letters: list) -> str:
    result = "".join([i if i in guessed_letters else '_' for i in word])
    return result


# Проверка на валидность буквы
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


# Функционал игры
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

if __name__ == "__main__":
    while True:
        if choose():
            word = get_word()
            if word is not None:
                play(word)
        else:
            print("До свидания!")
            break
