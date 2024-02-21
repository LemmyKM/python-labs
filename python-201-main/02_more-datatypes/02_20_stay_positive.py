# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]

positive = [n for n in numbers if n > 0]
print(positive)

# ander vb :

numbers = (1, 2, 3, 4, 5)
squares = [num**2 for num in numbers]
print(squares)