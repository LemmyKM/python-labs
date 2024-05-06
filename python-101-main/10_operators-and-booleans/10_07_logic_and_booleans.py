# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)


and_ = 2 < 1 and 3 < 4
print(and_)

or_ = 1 < 2 or 4 < 3
print(or_)

not_true = not True
print(not_true)

wrong = False
right = True

wrong_and_not_True = wrong + not_true
print(wrong_and_not_True)

mix = wrong + right
print(mix)


another_boolean = False and True or True and not False
print(another_boolean)