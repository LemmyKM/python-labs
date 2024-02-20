# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

from pathlib import Path
pad = Path.home() /'Python/CODINGNOMADS/labs/python-101-main/13_modules-and-automation'
for file in pad.iterdir():
    if file.suffix == '.py':
        print(file.name) # file.stem geeft enkel de naam zonder suffix

