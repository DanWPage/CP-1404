"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os
import shutil
from Prac_9 import file_fixer

EXCEPTIONS = ('.', '.\Lyrics', '.\__MACOSX', '.\__MACOSX\Lyrics', '.\__pycache__')

print("Current directory is", os.getcwd())
for dir_name, subdir_list, file_list in os.walk('.'):
    if dir_name not in EXCEPTIONS:
        print("In", dir_name)
        print("\tcontains subdirectories:", subdir_list)
        print("\tand files:", file_list)
        new_names = [file_fixer.get_fixed_filename(name) for name in file_list]
        print("\tchange to:", new_names)
