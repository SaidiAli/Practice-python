# What year are you turning 100???

current_yr = 2020

name = input('Enter your name: ')
age = int(input('Enter your age: '))

hundred_yr = current_yr + (100 - age)

print('Dear {}, you\'ll turn 100 years in the year {} \n'.format(name, hundred_yr))

num = int(input('How many time should the message be repeated: '))

print('Dear {}, you\'ll turn 100 years in the year {} \n'.format(name, hundred_yr) * num)
