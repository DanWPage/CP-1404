"""
    Word search. Getts a string from the user, puts each word in a dictionary and the number of times it
    occurs in the string.
"""

string = 'this is a collection of words of nice words this is a fun thing it is'
word_list = string.split()
Word_dict = {}
for word in word_list:
    if word not in Word_dict:
        Word_dict[word] = 1
    else:
        Word_dict[word] += 1
dict_to_list = []
for word in Word_dict:
    dict_to_list =
