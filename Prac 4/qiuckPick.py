"""
    'Quick Pick' lotto generator.
"""

import random

GAME_LENGTH = 6
HIGHEST_NUMBER = 45


def main():
    number_of_games = int(input('How many games? '))
    for i in range(number_of_games):
        game = get_game()
        print_game(sorted(game))


def get_game():
    game = []
    while len(game) < GAME_LENGTH:
        number = random.randint(1, HIGHEST_NUMBER)
        while number not in game:
            game.append(number)
    return game


def print_game(game):
    for number in game:
        print('{:3}'.format(number), end="")
    print()

main()
