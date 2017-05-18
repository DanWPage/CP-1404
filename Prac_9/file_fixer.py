

def get_fixed_filename(filename):

    # Replace spaces with underscores and .TXT lower case
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    namelist = list(new_name)
    # Make sure the first letter is upper case
    namelist[0] = namelist[0].capitalize()
    for i in range(len(namelist)-2, -1, -1):

        # Separates Pascal case words
        if namelist[i+1].isupper():
            if namelist[i].islower():
                namelist.insert(i+1, '_')

            # Check for 2 capitals together
            if namelist[i].isupper():
                namelist.insert(i+1, '_')

        # Make the first letters a capital
        if namelist[i] == '_':
            namelist[i+1] = namelist[i+1].capitalize()

    # Change the list back to a string
    fixed_name = ''
    for character in namelist:
        fixed_name = fixed_name + character

    # return the fixed file name
    return fixed_name


get_fixed_filename('in the little town blah')
