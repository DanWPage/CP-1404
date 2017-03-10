"""
Character to ascii/ ascii to character program.
"""

LOWER = 33
UPPER = 127


def main():
    menu_choice = menu()
    while menu_choice != "Q":
        if menu_choice == "A":
            ascii_to_char()
            menu_choice = menu()
        else:
            char_to_ascii()
            menu_choice = menu()
    print_all()
# --------------------------------------------------------------------------------------------


def menu():
    print("Enter 'C' to convert a character to ascii, 'A' to ascii to a character or 'Q' to quit.")
    choice = input("(A/C/Q):")
    while choice.upper() not in ["A", "C", "Q"]:
        choice = input("(A/C/Q):")
    return choice.upper()
# ---------------------------------------------------------------------------------------------


def ascii_to_char():
    ascii_num = int(input("Enter a number between {} and {} :".format(LOWER, UPPER)))
    while ascii_num < LOWER or ascii_num > UPPER:
        ascii_num = int(input("Enter a number between {} and {} :".format(LOWER, UPPER)))
    print("The character for ascii({}) is {}\n".format(ascii_num, chr(ascii_num)))
    return
# ---------------------------------------------------------------------------------------------


def char_to_ascii():
    character = input("Enter a character :")
    print("The ascii code for {} is {}\n".format(character, ord(character)))
    return
# ---------------------------------------------------------------------------------------------


def print_all():
    print("ASCII : CHARACTER")
    for i in range(LOWER, UPPER + 1):
        print("{:5} : {}".format(i, chr(i)))


main()
