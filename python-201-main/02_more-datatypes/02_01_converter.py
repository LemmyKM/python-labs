# Convert a string to a tuple and print out the result.
# What do you see?  The printout stays on one line with every letter between brackets.
# What happens if you try to iterate over your tuple of characters?  Every letter is printed out on a new line.
# Do you notice any difference to iterating over the string?

string = "codingnomads"
string_tup = tuple(string)
print(string_tup)

for char in string_tup:
    print(char)
