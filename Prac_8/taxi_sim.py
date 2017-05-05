from Prac_8.cars import Taxi
from Prac_8.cars import SilverServiceTaxi
from random import randint

TAXIS = [Taxi('Prius', 100),
         Taxi('Camary', 80),
         Taxi('Commodore', 100),
         Taxi('Falcon', 70),
         Taxi('Elantra', 60),
         SilverServiceTaxi('Hummer', 200, 4),
         SilverServiceTaxi('Audi A8', 100, 2),
         SilverServiceTaxi('Merc M8', 120, 3),
         SilverServiceTaxi('Limo', 100, 2),
         SilverServiceTaxi('Ferrari F40', 140, 6)]


def main():
    print('Lets drive!')
    choice = menu()
    while choice != "q":
        if choice == "c":
            show_taxis()


def menu():
    choice = input('q)uit, c)hoose taxi, d)rive')
    return choice

def show_taxis():
    for i in TAXIS:
        print(i, '-', TAXIS[i])
    return