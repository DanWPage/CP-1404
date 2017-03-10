

total = 0
number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Enter the number of items: "))
for i in range(number_of_items):
    item = float(input("Price of item?: "))
    total += item
if total > 100:
    total *= .9
print("Total price for {} items is ${:.2f}".format(number_of_items, total))
