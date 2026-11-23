from constants import STAGES


def display_hangman(mistakes: int) -> str:
   try:
      return STAGES[mistakes]
   except IndexError:
      return "Ошибка: количество ошибок превышает допустимое значение."



def word_update(word: str, guessed_letters: set) -> str:
   result = "".join([i if i in guessed_letters else '_' for i in word])
   return result
