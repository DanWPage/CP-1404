from Prac_8.cars import Taxi
from Prac_8.cars import SilverServiceTaxi

TAXIS = [Taxi('Prius', 100),
         SilverServiceTaxi('Limo', 100, 2),
         SilverServiceTaxi('Hummer', 200, 4),]


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
            taxi.start_fare()
            taxi.drive(distance)
            bill += taxi.get_fare()
            print('Your {} trip cost you ${:.2f}'.format(taxi.name, taxi.get_fare()))
        print('Bill to date: ${:.2f}'.format(bill))
        menu_choice = menu()
    print('Total trip cost: ${:.2f}'.format(bill))
    print('Taxis are now:')
    show_taxis()


def choose_taxi():
    choice = int(input('Choose taxi: '))
    return TAXIS[choice]


def get_distance():
    return int(input("Drive how far?"))


def menu():
    print('q)uit, c)hoose taxi, d)rive')
    choice = input('>>> ')
    return choice


def show_taxis():
    print('Taxis available:')
    for i in range(len(TAXIS)):
        print(i, '-', TAXIS[i])

main()
