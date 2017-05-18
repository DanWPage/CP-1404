import os
import shutil

os.chdir('FilesToSort')
files = os.listdir('.')
subfolders = []
for filename in files:
    extention = filename.split('.')[1]
    if extention not in subfolders:
        os.mkdir(extention)
        subfolders.append(extention)
    shutil.move(filename, extention)
