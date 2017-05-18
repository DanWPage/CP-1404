"""
    Returns the passed in string with spaces replaced with underscores, .TXT with.txt and separates pascal case words.
"""


def get_fixed_filename(filename):

    # Replace spaces with underscores and .TXT lower case
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    namelist = list(new_name)

    # Make sure the first letter is upper case
    namelist[0] = namelist[0].capitalize()
    for i in range(len(namelist)-2, -1, -1):
        if namelist[i+1].isupper() and namelist[i] != '_':
            namelist.insert(i+1, '_')

        # Make the first letter of each word a capital
        if namelist[i] == '_':
            namelist[i+1] = namelist[i+1].capitalize()

    alt_name = ''.join(namelist)
    # os.rename(filename, alt_name)
    return alt_name
