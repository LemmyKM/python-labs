# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

many_keys = {}

for n in range(1, 10):
    many_keys[n] = n * n

print(many_keys)
