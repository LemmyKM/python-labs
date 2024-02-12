# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

sentence = input('enter a sentence : ')
letter_input = input('choose a letter that is in the sentence you typed : ')
print()
index = sentence.find(letter_input)
print(f'String input : {sentence}')
print(f'Letter input : {letter_input}')
print(f'Result : {index}')
