

numbers = []
for i in range(5):
    numbers.append(int(input("Number: ")))
print('The first number is', numbers[0])
print('The last number is', numbers[-1])
print('The smallest number is', min(numbers))
print('The largest number is', max(numbers))
print('The average is', float(sum(numbers)/len(numbers)))
