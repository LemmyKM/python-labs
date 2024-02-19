sentence = input('enter a sentence : ')
no_spaces = sentence.replace(' ', '')
punct = ',.?!@#&'
analysis = {'lower_case': 0, 'upper_case': 0, 'punctuation' : 0, 'total_char' : 0}


for char in no_spaces:
    if char in punct:
        analysis['punctuation'] += 1
        analysis['total_char'] += 1
    elif char == char.upper():
        analysis['upper_case'] +=1
        analysis['total_char'] += 1
    elif char == char.lower():
        analysis['lower_case'] += 1
        analysis['total_char'] += 1



# for char in no_spaces:
#     if char == char.lower():
#         analysis['lower_case'] += 1
#         analysis['total_char'] += 1
#     elif char == char.upper():
#         analysis['upper_case'] += 1
#         analysis['total_char'] += 1
#     elif char in punct:
#         analysis['punctuation'] += 1
#         analysis['total_char'] += 1

#analysis['total_char'] = sum(analysis.values())

print(analysis)