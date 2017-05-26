"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))


def do_something(n):
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of this will be,
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)

# TODO: 5. fix the do_something() function so that it works the way it is probably supposed to :)


def do_something2(n):
    if n < 0:
        return
    do_something2(n-1)
    print(n**2)

do_something2(4)


def main():
    rows = int(input('How many rows? '))
    print('For {} rows, it is '.format(rows), end='')
    print(brick_counter(rows))


def brick_counter(n):
    if n == 1:
        print(n, '=', end=' ')
        return n
    print(n, '+', end=' ')
    return n + brick_counter(n-1)

# main()
