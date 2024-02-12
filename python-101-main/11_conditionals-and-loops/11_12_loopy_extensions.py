# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

has_pdf = False
check = ''

for char in filename:
    check += char
    if '.pdf' in check:
        has_pdf = True
print(has_pdf)








# has_pdf = False

# if '.pdf'  in filename:
#     has_pdf = True
#     print("It's a pdf!")


