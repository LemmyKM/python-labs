# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.


gen = (s for s in range(10))
for s in gen:
    print(s)