from Prac_8.cars import Taxi
from Prac_8.cars import SilverServiceTaxi

TAXIS = [Taxi('Prius', 100),
         SilverServiceTaxi('Hummer', 200, 4),
         SilverServiceTaxi('Limo', 100, 2)]


def main():
    bill = 0
    print('Lets drive!')
    menu_choice = menu()
    while menu_choice != "q":
        if menu_choice == "c":
            show_taxis()
            taxi = choose_taxi()
        elif menu_choice == "d":
            distance = get_distance()
            taxi.drive(distance)
            bill += taxi.get_fare()
        print('Bill to date: ${:.2f}'.format(bill))
        menu_choice = menu()


def choose_taxi():
    choice = int(input('Choose taxi: '))
    return TAXIS[choice]


def get_distance():
    return int(input("Drive how far?"))


def menu():
    choice = input('q)uit, c)hoose taxi, d)rive')
    return choice


def show_taxis():
    print('Taxis available:')
    for i in range(len(TAXIS)):
        print(i, '-', TAXIS[i])

main()
