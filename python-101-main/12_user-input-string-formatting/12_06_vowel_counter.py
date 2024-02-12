# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

userinput = input('enter a sentence : ')

counter = list(map(userinput.lower().count, 'aeiou'))
print(counter)

# of meteen printen :
print(*map(userinput.lower().count, 'aeiou'))

# zie de pdf over mapfunctie

"""!!! The first argument to map() is a function object,
which means that you need to pass a function without calling it.
That is, without using a pair of parentheses."""