"""
    Reads each line of 'numbers.txt' and adds them up.
"""

total = 0
number_file = open("numbers.txt", mode='r')
for i in number_file:
    i = int(i)
    total += i
number_file.close()
print(total)
