"""
    Daniel Page.
"""

name = ""
while not name:
    name = input("Enter your name :")
for i in range(0, len(name), 2):
    print(name[i], end="")
