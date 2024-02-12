# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

def number():
    n = int(input('enter a number : '))
    for cijfer in range(1, n):
        if cijfer % 3 == 0 and cijfer % 5 == 0:
            print('FizzBuzz')
        elif cijfer % 3 == 0:
            print('Fizz')
        elif cijfer % 5 == 0:
            print('Buzz')
        else:
            print(cijfer)

number()