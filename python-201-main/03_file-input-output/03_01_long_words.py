# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


from pathlib import Path

file_path = Path.home() / 'Python/CODINGNOMADS/labs/python-201-main/03_file-input-output/words.txt'
with open(file_path, mode='r', encoding='utf-8') as file:
    word = file.readlines()
    for w in word:
        if len(w) > 20:
            print(w, end='')
