import random as r

# Запрос юзера продолжить/закончить игру
def choose():
    while True:
        choose = input("Начать новую игру/Выйти (Start/Exit): ")
        if choose.lower() in ["start", "s", "старт"]:
            return True
        elif choose.lower() in ["exit", "e", "выход"]:
            return False
        else:
            print("Вы ввели неправильный ответ")





# Выбор случайного слова с файла
def get_word():
    with open ("gamewords.txt", "r", encoding="utf-8") as f:
        word = r.choice(f.read().split()).upper()
        return word


# Функция получения текущего состояния
def display_hangman(tries):
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
def word_update(word, guessed_letters):
    result = "".join([i if i in guessed_letters else '_' for i in word])
    return result


# Проверка на валидность буквы
def is_valid_letter(guessed_letters, missed_letters):
    while True:
        user_input = input("Введите букву: ").upper()

        if user_input not in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
            print("Вы ввели не букву!")
        elif user_input in guessed_letters:
            print("Вы уже называли эту букву!")
        elif user_input in missed_letters:
            print("Этой буквы нету в слове, вы ее уже называли")
        else:
            return user_input


# Функционал игры
def play(word):
    guessed = False
    guessed_letters = []
    missed_letters = []
    tries = 6

    print("Добро пожаловать в игру 'Виселица'!")


    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_update(word, guessed_letters))
        print(f"Попыток осталось: {tries}")
        user_input = is_valid_letter(guessed_letters, missed_letters)

        if user_input in word:
            guessed_letters.append(user_input)
            print("Верно! Буква", user_input, "есть в слове.")
            if word_update(word, guessed_letters).count("_") == 0:
                guessed = True
                print("Поздравляем, вы угадали слово! Вы победили!")
                break

        else:
            if user_input not in missed_letters:
                tries -= 1
                print("Буквы", user_input, "нет в слове.")
                missed_letters.append(user_input)
            else:
                print("Вы уже называли эту букву, ее нету в слове")
            if tries == 0:
                print("Вы проиграли! Загаданное слово было:", word)
                break

while True:
    if choose():
        play(get_word())
    else:
        print("До свидания!")
        break
