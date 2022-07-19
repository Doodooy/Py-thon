# Made by aryaman :)
import random
import time
print('Welcome to the Snake and Water game!')
t1 = int(input('Your Turn: \n 1. Snake \n 2. Water \n 3. Gun\n-> '))
t2 = random.randint(1, 3)
win_plyr = 'You win!'

win_comp = 'Computer wins!'

tie = 'It\'s a tie!'


def game(a,b):
    print(f'\nYou chose {a}\n')
    time.sleep(.5)
    print(f'The computer chose {b}\n')
    time.sleep(.5)
    if a == b:
        print(tie)
    elif a == 1 and b == 2:
        print(win_plyr)
    elif a == 2 and b == 1:
        print(win_comp)
    elif a == 2 and b == 3:
        print(win_plyr)
    elif a == 3 and b == 2:
        print(win_comp)
    elif a == 3 and b == 1:
        print(win_plyr)
    elif a == 1 and b == 3:
        print(win_plyr)
    else:
        print('Please choose an option using 1,2 or 3')

game(t1,t2)