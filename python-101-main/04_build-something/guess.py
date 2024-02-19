# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random
number = random.randint(1, 10)
guess = None

while guess != number:
    guess = input("guess a number between 1 and 10 : ")
    guess = int(guess)
    if guess == number:
        print("Congrats! You won!")
        break
    else:
        print("Try again!")