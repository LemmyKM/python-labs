# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

# largest number
largest_number = randlist
max_number = max(largest_number)
print(max_number)

# product all numbers
result = 1
for x in largest_number:
    result = result * x
print(result)


#print(randlist)
