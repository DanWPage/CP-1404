import os
import shutil

os.chdir('FilesToSort')
files = os.listdir('.')
categories = {}
for filename in files:
    extension = filename.split('.')[1]
    if extension not in categories:
        directory = input('What category would you like to put {} files into? '.format(extension))
        categories[extension] = directory
        if directory not in categories.values():
            os.mkdir(directory)
    # print(filename, 'moved to', categories[extension])
    print(categories)
    shutil.move(filename, categories[extension])
