

def main():
    start = get_number('x')
    stop = get_number('y')
    menu_choice = menu()
    while menu_choice != '4':
        if menu_choice == '1':
            show_evens(start, stop)
        elif menu_choice == '2':
            show_odds(start, stop)
        else:  # menu_choice == '3'
            show_squares(start, stop)
        menu_choice = menu()


def menu():
    print('Do you want to;\n'
          '1. Show the even numbers from x to y\n'
          '2. Show the odd numbers from x to y\n'
          '3. Show the squares from x to y\n'
          '4. Exit the program')
    choice = input('>>> ')
    while choice not in ('1', '2', '3', '4'):
        choice = input('You must enter 1, 2, 3 or 4')
    return choice


def show_evens(start, stop):
    if start < stop:  # counting up
        if start % 2 == 1:
            start += 1
        stop += 1
        step = 2
    else:  # counting down
        if start % 2 == 1:
            start -= 1
        stop -= 1
        step = -2
    for i in range(start, stop, step):
        print(i, end=' ')
    print('\n')


def show_odds(start, stop):
    if start < stop:  # counting up
        if start % 2 == 0:
            start += 1
        stop += 1
        step = 2
    else:  # counting down
        if start % 2 == 0:
            start -= 1
        stop -= 1
        step = -2
    for i in range(start, stop, step):
        print(i, end=' ')
    print('\n')


def show_squares(start, stop):
    if start < stop:  # counting up
        stop += 1
        step = 1
    else:  # counting down
        stop -= 1
        step = -1
    for i in range(start, stop, step):
        print(i**2, end=' ')
    print('\n')


def get_number(description):
    number = input('Enter {}: '.format(description))
    while not isinstance(number, int):  # This is really a while True but describes what we're looking for.
        try:
            return int(number)
        except ValueError:
            number = input('You must enter an integer: ')

main()
