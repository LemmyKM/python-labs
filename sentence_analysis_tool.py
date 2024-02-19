# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

from string import ascii_uppercase, ascii_lowercase, punctuation
sentence = input('enter a sentence : ')
# punct = ',.?!@#&'
analysis = {'lower_case': 0, 'upper_case': 0, 'punctuation' : 0, 'total_char' : 0}

for char in sentence:
    if char in punctuation:
        analysis['punctuation'] += 1
        analysis['total_char'] += 1
    elif char in ascii_lowercase:
        analysis['lower_case'] += 1
        analysis['total_char'] += 1
    elif char in ascii_uppercase:
        analysis['upper_case'] += 1
        analysis['total_char'] += 1





# for char in no_spaces:
#     if char in punct:
#         analysis['punctuation'] += 1
#         analysis['total_char'] += 1
#     elif char == char.upper():
#         analysis['upper_case'] +=1
#         analysis['total_char'] += 1
#     elif char == char.lower():
#         analysis['lower_case'] += 1
#         analysis['total_char'] += 1


# analysis['total_char'] = sum(analysis.values())

print(analysis)