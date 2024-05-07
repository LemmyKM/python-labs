# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it


# hangman.py

from random import choice
import string

def select_word():
    with open('words.txt', mode='r') as words:
        word_list = words.readlines()
    return choice(word_list).strip()

def get_player_input(guessed_letters):
    while True:
        player_input = input('Guess a letter : ').lower()
        if _validate_input(player_input, guessed_letters):
            return player_input
# !'get_player_input' en '_validate_input' hangen af van elkaar! zie RealPython pdf!!!
def _validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )
        
def join_guessed_letters(guessed_letters):
    return ' '.join(sorted(guessed_letters))

def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append('_')
    return ' '.join(current_letters)

def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
------
""",
        r"""
  -----
  |   |
  0   |
      |
      |
      |
      |
      |
      |
      |
------
""",
        r"""
  -----
  |   |
  0   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
------
""",
        r"""
  -----
  |   |
  0   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
------
""",
        r"""
  -----
  |   |
  0   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
------
""",
        r"""
  -----
  |   |
  0   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
------
""",
        r"""
  -----
  |   |
  0   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
------
""",
    ]
    
    print(hanged_man[wrong_guesses])

MAX_INCORRECT_GUESSES = 6

def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False

if __name__ == '__main__':
    # Initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print('Welcome to Hangman!')

    # Game loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is : {guessed_word}")
        print(
            'Current guessed letters : '
            f'{join_guessed_letters(guessed_letters)}\n'
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print('Great guess!')
        else:
            print('Sorry, it\'s not there.')
            wrong_guesses += 1
        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # Game over
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print('Sorry, you lost!')
    else:
        print('Congrats! You did it!')
    print(f'Your word was : {target_word}')

