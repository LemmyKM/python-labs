import string
#from string import ascii_lowercase, ascii_uppercase,

sentence = input('enter a sentence : ')
analysis = {'lower_case': 0, 'upper_case': 0, 'punctuation' : 0, 'total_char' : 0}

for char in sentence:
    if char in string.punctuation:
        analysis['punctuation'] += 1
        analysis['total_char'] += 1
    elif char in string.ascii_uppercase:
        analysis['upper_case'] +=1
        analysis['total_char'] += 1
    elif char in string.ascii_lowercase:
        analysis['lower_case'] += 1
        analysis['total_char'] += 1



# analysis['total_char'] = sum(analysis.values())

print(analysis)