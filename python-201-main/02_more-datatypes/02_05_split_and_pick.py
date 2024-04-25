# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

from collections import Counter

userinput = input('Enter a sentence : ')

lijstje = userinput.split()
print(lijstje)

# print most common word :
common = Counter(lijstje)
print(common)

