"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Lindsay Ward'


def main():
    choice = get_menu_choice()
    while choice != "q":
        if choice == "c":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        else:
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        choice = get_menu_choice()menu()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def get_menu_choice():
    print("\nC - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)")
    choice = input(">>> ")
    while choice.lower() not in ["q", "c", "f"]:
        choice = input(">>> ")
    return choice.lower()


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()
