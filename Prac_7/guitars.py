from Prac_7.guitar import Guitar


def main():
    my_guitars = []
    print('My Guitars!')
    name = input('Name: ')
    while name != '':
        year = input('Year: ')
        cost = input('Cost: ')
        my_guitars.append(Guitar(name, year, cost))
        name = input('Name: ')
    # enumerate returns a tuple (index, value) from an iterable object
    # enumerate(object, start=0) where start is the first index given to the first value
    for i, guitar in enumerate(my_guitars):
        print('Guitar {}: {:>20} ({}), worth ${:10,.2f}'.format(i + 1, guitar.name, guitar.year, guitar.cost))


main()
