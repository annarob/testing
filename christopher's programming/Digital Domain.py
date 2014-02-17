#This game
import pickle
import random
import time
global coins
coins = 25
dailyBonus = (random.randint(0, coins))
def install():
    print('Would you like continue game?')
    response = input()
    if response == 'yes':
       print('Saving is in development.')
    else:
        print('Type in your username.')
        username = input()
        print('Hello, ' +username)
        print('coins:' +(str(coins)))
        print('daily bonus:'+(str(dailyBonus)))
        coins = coins + dailyBonus
        print('coins:'+coins)
install()
