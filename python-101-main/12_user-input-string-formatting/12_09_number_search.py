# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = int(input('enter a number between 0 and 1,000,000,000 : '))

while number not in range(1, 1000000001):
    number = int(input('That is not in the specified range. Please try again : '))

print(f"The number you chose is {number:,}.\n")             