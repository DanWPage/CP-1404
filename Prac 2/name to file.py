"""
    Asks user for their name and writes it to 'name.txt'
"""

name = input("What is your name?")
print("We are watching you {}".format(name))
name_file = open("name.txt", mode='w')
print(name, file=name_file)
name_file.close()
