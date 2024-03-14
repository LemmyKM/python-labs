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
    total_words = len(words)
    for w in words:
        lengte_word = lengte.append(len(w))
        if len(w) == 3:
            print(w, end='')
        elif len(w) == 22:
            print(w, end='')
        else:
            pass

kortst = min(lengte)
langst = max(lengte)

print(f"Total number of words = {total_words}")
print(f"Shortest word = {kortst}")
print(f"Longest word = {langst}")
