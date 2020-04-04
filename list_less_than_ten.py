# List comprehension
original = [i**2 for i in range(1, 10)]  
num = int(input('Enter a number: '))
new = [i for i in original if i < num]

print(new)