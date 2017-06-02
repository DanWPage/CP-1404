
def main():
    menu = "Choose an option:\n" \
       "(L) Left\n" \
       "(R) Right\n" \
       "(F) Forward\n" \
       "(Q) Quit"
    print(menu)
    choice = get_choice()
    while choice != 'q':
        if choice == 'l':
            print("Go left")
        elif choice == 'r':
            print("Go right")
        else:
            print("Go forward")
        print(menu)
        choice = get_choice()


def get_choice():
    choice = input("?").lower()
    while choice not in ["l", "r", "f", "q"]:
        print("You must choose either L, R, F or Q")
        choice = input("?").lower()
    return choice

main()

