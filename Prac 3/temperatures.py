"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'


def main():
    choice = menu()
    while choice != "q":
        if choice == "c":
            fahrenheit = celsius_to_fahrenheit()
            print("Result: {:.2f} F".format(fahrenheit))
        else:
            celsius = fahrenheit_to_celsius()
            print("Result: {:.2f} C".format(celsius))
        choice = menu()
    print("Thank you.")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def menu():
    MENU = "\nC - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ")
    while choice.lower() not in ["q", "c", "f"]:
        choice = input(">>> ")
    return choice.lower()


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
