"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    print("Use c for consonants, v for vowels.")
    word_format = input("Enter a sequence:")
    while not is_valid_format(word_format):
        print("Use c or v only")
        word_format = input("Enter a sequence:")
    word = ""
    for kind in word_format.lower():
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(word_format):
    for char in word_format:
        if char.lower() not in ["c", "v"]:
            return False
        return True

main()
