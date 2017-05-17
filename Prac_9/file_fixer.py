import os

# filename = HarkTheHerold


def get_fixed_filename(filename='HarkTheHerold'):
    namelist = list(filename.upper())
    for i in range(len(namelist)-2, 0, -1):

        # Separates Pascal case words
        if str(namelist[i+1]).isupper():
            namelist.insert(i+1, '_')

    # Change the list back to a string
    fixed_name = ''
    for character in namelist:
        fixed_name = fixed_name + character

    return fixed_name

# get_fixed_filename()
