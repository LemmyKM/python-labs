# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

user_input = int(input('enter a figure between 1 and 1,000,000,000 : '))
print()
while user_input < 1 or user_input > 1000000000:
    user_input = int(input('That is not correct. Try again : '))
print()
if user_input % 3 == 0:
    print(f"{user_input} / 3 = {user_input/3:.0f}")
else:
    print('The figure you entered is not divisible by 3')