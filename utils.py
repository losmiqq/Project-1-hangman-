

def display_hangman(mistakes: int) -> str:
    stages = [
        # 0 ошибок
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        ''',

        # 1 ошибка
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',

        # 2 ошибки
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',

        # 3 ошибки
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',

        # 4 ошибки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',

        # 5 ошибок
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',

        # 6 ошибок
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        '''
    ]

    return stages[mistakes]


# Состояние загаданного слова
def word_update(word: str, guessed_letters: list) -> str:
    result = "".join([i if i in guessed_letters else '_' for i in word])
    return result
