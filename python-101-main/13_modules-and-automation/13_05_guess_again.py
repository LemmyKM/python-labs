# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
import sys

print()
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 0 and 100.")
max_number_of_guesses = 9

while True:
    guess = int(input('Enter your guess : \n'))
    if guess == secret_number:
        print(f"You win! The number is '{secret_number}'.")
        break
    elif guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    if max_number_of_guesses == 0:
        print('You loose!')
        break
    max_number_of_guesses -= 1


sys.exit()
