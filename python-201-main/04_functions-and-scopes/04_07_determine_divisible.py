# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


userinput = int(input('Enter a number between 1 and 1,000,000,000 : '))

def divide(userinput):
    one = userinput % 4 == 0 or userinput % 7 == 0
    print(one)
    two = userinput % 4 == 0 and userinput % 7 == 0
    print(two)
    if one == True:
        print(f"{userinput} can be divided by 4 OR 7.")
    else:
        print(f"{userinput} can NOT be divided by 4 or 7.")
    if two == True:
        print(f"{userinput} can be divided by 4 AND by 7.")
    else:
        print(f"{userinput} can NOT be divided by 4 AND by 7.")
    
    
divide(userinput)