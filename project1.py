import random as r

def choose():
    while True:
        choose = input("Начать новую игру/Выйти (Start/Exit): ")
        if choose.lower() in ["start", "s", "старт"]:
            return True
        elif choose.lower() in ["exit", "e", "выход"]:
            return False
        else:
            print("Вы ввели неправильный ответ")


word_list = word_list = [
    "велосипед", "компьютер", "алгоритм", "интернет", "клавиатура", 
    "телефон", "самолёт", "автомобиль", "поезд", "корабль", "рюкзак", 
    "холодильник", "телевизор", "пылесос", "зеркало", "кровать", "диван", 
    "собака", "кошка", "медведь", "слон", "жираф", "крокодил", "пингвин", 
    "дельфин", "акула", "черепаха", "яблоко", "апельсин", "банан", "арбуз", 
    "картофель", "морковь", "помидор", "огурец", "шоколад", "бутерброд", 
    "дерево", "цветок", "радуга", "облако", "гора", "водопад", "океан", 
    "остров", "космос", "планета"
    ]

def get_word(word_list):
    return r.choice(word_list).upper() 


# функция получения текущего состояния
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




def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Добро пожаловать в игру 'Виселица'!")


    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_completion)
        user_input = input("Введите букву или слово целиком: ").upper()
        for i in user_input:
            if not i.isalpha():
                print("Вы ввели не букву!")
                user_input = input("Введите букву или слово целиком: ").upper()
                break

        for i in user_input:
            if i in guessed_letters:
                print("Вы уже называли букву", i)
                user_input = input("Введите букву или слово целиком: ").upper()
                break

            elif i in word:
                guessed_letters.append(i)
                print("Верно! Буква", i, "есть в слове.")
                word_completion = ''.join([i if i in guessed_letters else '_' for i in word])
                print(word_completion)
                if '_' not in word_completion:
                    guessed = True
                    print("Поздравляем, вы угадали слово! Вы победили!")
                    break

            else:
                tries -= 1
                print("Буквы", i, "нет в слове.")
                if tries == 0:
                    print("Вы проиграли! Загаданное слово было:", word)
                    break

while True:
    if choose():
        play(get_word(word_list))
    else:
        print("До свидания!")
        break