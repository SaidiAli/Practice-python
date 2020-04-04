# Rock paper scissor

def check(str1, str2):
    if(str1 == 'rock' and str2 == 'paper'):
        return print('Paper beats rock: Player two wins.')
    elif (str1 == 'paper' and str2 == 'rock'):
        return print('Paper beats rock: Player one wins.')
    elif (str1 == 'rock' and str2 == 'scissor'):
        return print('Rock beats scissor: Player one wins.')
    elif (str1 == 'scissor' and str2 == 'rock'):
        return print('Rock beats scissor: Player two wins.')
    elif (str1 == 'paper' and str2 == 'scissor'):
        return print('Scissor beats paper: Player two wins.')
    elif (str1 == 'scissor' and str2 == 'paper'):
        return print('Scissor beats paper: Player one wins.')

while(1):
    str1 = input('Player one: ')
    str2 = input('Player two: ')

    check(str1, str2)
    stop = input('Play again (y/n): ')
    if (stop == 'y'):
        continue
    elif (stop == 'n'):
        print('Quiting game: Thanks for playing...')
        break
    else:
        print('Wrong input!!')
        continue

