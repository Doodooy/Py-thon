
import random
import time


print('Welcome to the Snake and Water game!')

time.sleep(.5)


print('Press ENTER to begin')

input('')

time.sleep(1)

# t1 => input from user
# t2 => input from computer (random)
 

t1 = int(input('Your Turn: \n 1. Snake \n 2. Water \n 3. Gun\n\n-> '))
t2 = random.randint(1, 3)

# Winning/losing/tie statement

win_plyr = 'You win!'

win_comp = 'Computer wins!'

tie = 'It\'s a tie!'

# Game function

def game(a,b):
    
    if a == 1:
        option_plyr = 'Snake'
    elif a == 2:
        option_plyr = 'Water'
    elif a == 3:
        option_plyr = 'Gun'
    
    if b == 1:
        option_comp = 'Snake'
    elif b == 2:
        option_comp = 'Water'
    elif b == 3:
        option_comp = 'Gun'
    
    print(f'\nYou chose {option_plyr}\n')
    time.sleep(1)
    print(f'The computer chose {option_comp}\n')
    time.sleep(1)
    
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
