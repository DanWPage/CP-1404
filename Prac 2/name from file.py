

name_file = open("name.txt", mode='r')
name = name_file.read()
name_file.close()
print("Your name is {}".format(name))
print("I told you we were watching you")
