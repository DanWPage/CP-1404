"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

(Another way to get just consonants would be to use string.ascii_lowercase (all letters) and remove the vowels)
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"



print("Use % for consonents, # for vowels or * for either. You also enter any characters you want.")
word_format = input("Enter the format: ")
word = ""
for kind in word_format.lower():
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(CONSONANTS + VOWELS)
    else:
        word += kind
print(word)
