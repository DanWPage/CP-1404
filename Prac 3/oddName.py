"""
    Daniel Page.
"""


def main():
    name = get_name()
    increment = get_increment()
    print_name(name)


def print_name(name):
    for i in range(0, len(name), 2):
        print(name[i], end="")


def get_increment():
    invalid = True
    while invalid:
        try:
            number = int(input("Enter the increment: "))
            return number
        except ValueError:
            pass


def get_name():
    name = ""
    while not name:
        name = input("Enter your name :")
    return name


main()
