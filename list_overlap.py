import random as r

list_one = [i**2 for i in range(1, 10)]
list_two = r.sample(range(80), 9)

new_list = [i for i in list_one if i in list_two]

print(new_list)