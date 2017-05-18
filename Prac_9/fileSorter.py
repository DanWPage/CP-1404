import os
import shutil

os.chdir('FilestoSort')
files = os.listdir('.')
subfolders = []
for filename in files:
    extention = filename.split('.')[1]
    if extention not in subfolders:
        os.mkdir(extention)
        subfolders.append(extention)
    shutil.move(filename, extention)
