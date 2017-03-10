"""
    Reads each line of 'numbers.txt' and adds them up.
"""

total = 0
number_file = open("numbers.txt", mode='r')
for line_number in number_file:
    line_number = int(line_number)
    total += line_number
number_file.close()
print(total)
