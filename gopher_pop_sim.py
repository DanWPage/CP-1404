"""
    Gopher Population Simulator
"""

import random

YEARS = 10
STARTING_POP = 1000
BIRTH_LOWER = .1
BIRTH_UPPER = .2
DEATH_LOWER = .05
DEATH_UPPER = .25


def main():
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population:", STARTING_POP)
    population = STARTING_POP
    for year in range(YEARS):
        print("\nYear", year + 1)
        print("*" * 5)
        births = get_births(population)
        deaths = get_deaths(population)
        population = population + births - deaths
        print("{} gophers were born. {} died".format(births, deaths))
        print("Population:", population)


def get_births(pop):
    births = int(pop * random.uniform(BIRTH_LOWER, BIRTH_UPPER))
    return births


def get_deaths(pop):
    deaths = int(pop * random.uniform(DEATH_LOWER, DEATH_UPPER))
    return deaths


main()
