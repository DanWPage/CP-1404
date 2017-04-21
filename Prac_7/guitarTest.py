
from Prac_7.guitar import Guitar

gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)

print(gibson)

print('The {} is {} years old'.format(gibson.name, Guitar.get_age(gibson)))
print('expected age is', 2017 - gibson.year)

print('is_vintage is {}: expected {}'.format(gibson.is_vintage(), True))
