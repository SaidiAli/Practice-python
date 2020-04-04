# Guess a number in the range of 1-9
import random as r
import sys

r.sample

count = 0

while 1:
    guess = input('Guess a number: ')
    num = r.randint(1, 9)

    if guess == str(num):
        print('Thats right!!!')
        print('You made {} guesses'.format(count))
        break
    # 'exit' to quit game
    elif guess == 'exit':
        print('You made {} guesses'.format(count))
        print('Exiting: Thanks for playing')
        break
    else:
        print('Wrong, the number is: {} Try again'.format(num))
        count = count + 1
        continue

sys.exit()