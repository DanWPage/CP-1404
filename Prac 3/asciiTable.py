"""
Character to ascii/ ascii to character program.
"""



def main():
    LOWER = 33
    UPPER = 127
    menu_choice = menu()
    while menu_choice != "Q":
        if menu_choice == "A":
            ascii_num = get_number(LOWER, UPPER)
            print("The character for ascii({}) is {}\n".format(ascii_num, chr(ascii_num)))
        else:
            char_to_ascii()
        menu_choice = menu()
    print_all(LOWER, UPPER)
# --------------------------------------------------------------------------------------------


def menu():
    print("Enter 'C' to convert a character to ascii, 'A' to ascii to a character or 'Q' to quit.")
    choice = input("(A/C/Q):")
    while choice.upper() not in ["A", "C", "Q"]:
        choice = input("(A/C/Q):")
    return choice.upper()
# ---------------------------------------------------------------------------------------------


def char_to_ascii():
    character = input("Enter a character :")
    print("The ascii code for {} is {}\n".format(character, ord(character)))
    return
# ---------------------------------------------------------------------------------------------


def print_all(lower, upper):
    print("ASCII : CHARACTER")
    for i in range(lower, upper + 1):
        print("{:5} : {}".format(i, chr(i)))
# ---------------------------------------------------------------------------------------------


def get_number(lower, upper):
    invalid = True
    while invalid:
        try:
            number = int(input("Enter a number from {} to {} :".format(lower, upper)))
            if lower <= number <= upper:
                return number
        except ValueError:
            pass
        print("Enter a valid number")
# ---------------------------------------------------------------------------------------------


main()
