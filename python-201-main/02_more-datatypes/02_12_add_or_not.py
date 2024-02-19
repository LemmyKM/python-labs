# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

input_list = set()
allowed_input = range(1, 50)
number = int(input('enter a number from 1 to 50 : '))

while number not in allowed_input:
    number = input('that is not a number from 1 to 50. Try again : ')
    

