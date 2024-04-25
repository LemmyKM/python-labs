"""write a script that locates your Desktop, fetches all the files
that are on there, and counts how many files of each different 
file type are on your desktop. Use a dictionary to collect this data,
and print it to your console at the end in order to get an overview of
what is there.
If more than five different file types are present move them in their
own folder."""

from pathlib import Path
import shutil
import sqlalchemy

path_bureaublad = Path.home() /'Desktop'
path_strayfiles_folder = Path.home() /'Desktop'/'strayfiles'
path_png_folder = Path.home() /'Desktop/png_folder'
path_app_folder = Path.home() /'Desktop/app_folder'
path_txt_folder = Path.home() /'Desktop/txt_folder'
path_doc_folder = Path.home() /'Desktop/doc_folder'
path_pdf_folder = Path.home() /'Desktop/pdf_folder'
path_tif_folder = Path.home() /'Desktop/tif_folder'


file_type = {'png': 2, 'app': 1, 'txt': 4, 'doc': 3, 'pdf': 5, 'tif': 7}

# for file in path_bureaublad.iterdir():
#     if file.suffix == '.png':
#        path_png_folder.mkdir(exist_ok=True)
#        shutil.move(file, path_png_folder)
#        file_type['png'] +=1
    # elif file.suffix == '.app':
    #     path_app_folder.mkdir(exist_ok=True)
    #     shutil.move(file, path_app_folder)
#        file_type['app'] += 1
    # elif file.suffix == '.txt':  
    #     path_txt_folder.mkdir(exist_ok=True)
    #     shutil.move(file, path_txt_folder)
#        file_type['txt'] += 1
    # elif file.suffix == '.docx':  
    #     path_doc_folder.mkdir(exist_ok=True)
    #     shutil.move(file, path_doc_folder)
#        file_type['docx'] += 1
    # elif file.suffix == '.pdf':  
    #     path_pdf_folder.mkdir(exist_ok=True)
    #     shutil.move(file, path_pdf_folder)
#        file_type['pdf'] += 1
    # elif file.suffix == '.tif':  
    #     path_tif_folder.mkdir(exist_ok=True)
    #     shutil.move(file, path_tif_folder)
    #     file_type['tif'] += 1
    # else:
    #     path_strayfiles_folder.mkdir(exist_ok=True)
    #     shutil.move(file, path_strayfiles_folder)
#        file_type['strayfiles'] += 1


engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/file_counter')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
# table:
file_count = sqlalchemy.Table('file_count', metadata, autoload_with=engine)

insert_stmts = [
    file_count.insert().values(file_suffix=key, nr_suffix=value)
    for key, value in file_type.items()
]
for stmt in insert_stmts:
    connection.execute(stmt)

connection.commit()
connection.close()