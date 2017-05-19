import os


def main():
    os.chdir('Lyrics')
    for dir_name, subdir_list, file_list in os.walk('.'):
        for directory in subdir_list:
            os.chdir(directory)
            for file_name in file_list:
                with open(file_name) as data:
                    lines = data.readlines()
                    for line in lines:
                        if not line.startswith('.i'):
                            print('No copyright info in {}'.format(file_name))
