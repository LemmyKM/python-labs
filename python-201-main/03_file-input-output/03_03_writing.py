# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


from pathlib import Path

file_path = Path.home() / 'Python/CODINGNOMADS/labs/python-201-main/03_file-input-output/words.txt'
new_file = Path.home() / 'Python/CODINGNOMADS/labs/python-201-main/03_file-input-output/words_reverse.txt'

with open(file_path, mode='r', encoding='utf-8') as file:
    tekst = file.readlines()

with open(new_file, mode='w', encoding='utf-8') as w_reverse:
    w_reverse.writelines(tekst[::-1])
