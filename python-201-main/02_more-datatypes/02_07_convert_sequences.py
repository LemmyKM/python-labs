# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

string_to_tuple = tuple(string)
print(string_to_tuple)

tuple_to_list = list(string_to_tuple)
print(tuple_to_list)
print(string.replace('c', 'k'))