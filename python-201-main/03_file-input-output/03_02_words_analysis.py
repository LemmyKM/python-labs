# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


from pathlib import Path

lengte = []

file_path = Path.home() / 'Python/CODINGNOMADS/labs/python-201-main/03_file-input-output/words.txt'
with open(file_path, mode='r', encoding='utf-8') as file:
    words = file.readlines()
    for w in words:
        lengte_word = len(w)
        lengte.append(lengte_word)

shortest = min(lengte)
longest = max(lengte)
print()

with open(file_path, mode='r', encoding='utf-8') as file:
    words = file.readlines()
    for w in words:
        if len(w) == shortest:
            print(w, end='')
        elif len(w) == longest:
            print(w, end='')


print(f"SHORTEST word is {shortest} char long.")
print(f"LONGEST word is {longest} char long.")
print(f"TOTAL number of words is {len(lengte)}")