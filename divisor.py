num = int(input('Please enter a number: '))
div = [i for i in range(1, num) if num % i == 0]

print(div)