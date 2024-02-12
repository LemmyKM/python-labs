# guess the number.py

import random

def ask_for_guess():
    while True:
        guess = input('> ')
        if guess.isdecimal():
            return int(guess)
        print('please enter a figure between 1 and 100.')
print()
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

for i in range(10):
    print(f"You have {10-i} guesses left. Take a guess.")

    guess = ask_for_guess()

    if guess == secret_number:
        break
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

if guess == secret_number:
    print('You won!!!')
else:
    print(f"Game over! The number I was looking for is {secret_number}")