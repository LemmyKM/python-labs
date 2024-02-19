import pathlib
import shutil

# scrnshot = pathlib.Path('/Users/lemmy/Desktop/screenshots')
# scrnshot.mkdir(exist_ok=True)
# docs = pathlib.Path('/Users/lemmy/Documents')
# for file in docs.iterdir():
#     if file.suffix == '.png':
#         new_filepath = scrnshot.joinpath(file.name)
#         file.replace(new_filepath)

# of :
        
scrnshot = pathlib.Path('/Users/lemmy/Desktop/screenshots')
scrnshot.mkdir(exist_ok=True)
docs = pathlib.Path('/Users/lemmy/Documents')
for file in docs.iterdir():
    if file.suffix == '.png':
        shutil.move(docs, scrnshot)
