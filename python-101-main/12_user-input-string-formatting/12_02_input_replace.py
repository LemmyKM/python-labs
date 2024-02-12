# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


string_input = input('enter a sentence : ')
symbol = input('enter a symbol : ')
first_letter = string_input[0]

final = string_input.replace(first_letter, symbol)
print(final)