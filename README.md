# Hangman Game

A simple console-based Hangman game written in Python.

## Description

The player has to guess a hidden word by entering one Cyrillic letter at a time.

The word is randomly selected from the `gamewords.txt` file. Words shorter than 5 characters are excluded, and only words written in Cyrillic are accepted.

The player has 6 attempts to guess the word.

## Features

* Random word selection
* Support for Cyrillic letters
* Input validation
* Detection of previously entered letters
* Hangman drawing in the console
* Exclusion of words shorter than 5 characters
* Validation of words written only in Cyrillic
* Error handling for a missing or empty word file
* Modular project structure
* The game can be started or exited from the main menu

## Project Structure

```text
project/
├── main.py
├── game.py
├── word_manager.py
├── utils.py
├── constants.py
├── gamewords.txt
└── README.md
```

* `main.py` — application entry point
* `game.py` — main game logic and user input validation
* `word_manager.py` — reading, validating, and selecting words
* `utils.py` — helper functions for the game
* `constants.py` — game constants
* `gamewords.txt` — list of words used in the game
* `README.md` — project documentation

## Requirements

* Python 3.14
* No external libraries are required

## How to Run

Clone the repository and run:

python `main.py`

## How to Play

When the game starts, choose:

* `Start`, `S`, or `Старт` — start a new game
* `Exit`, `E`, or `Выход` — exit the game

During the game, enter one Cyrillic letter at a time.

If the letter is in the hidden word, it will be revealed. Otherwise, one attempt will be lost.

The game ends when:

* the player guesses the entire word;
* the player makes 6 incorrect guesses.

## Error Handling

The program handles cases where:

* `gamewords.txt` does not exist;
* the word file is empty;
* the file does not contain suitable words.

