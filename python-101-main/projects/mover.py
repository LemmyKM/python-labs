# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

import pathlib
import shutil
        
scrnshot = pathlib.Path('/Users/lemmy/Desktop/screenshots')
scrnshot.mkdir(exist_ok=True)
docs = pathlib.Path('/Users/lemmy/Documents')
for file in docs.iterdir():
    if file.suffix == '.png':
        shutil.move(file, scrnshot)