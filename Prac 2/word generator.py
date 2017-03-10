"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word_format = input("Enter the format. e.g.ccvc: ")
word = ""
for kind in word_format.lower():
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)