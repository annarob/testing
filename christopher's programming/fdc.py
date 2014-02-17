import time
import random
import sys
print('welcome to number ninja. copyright cbroc inc.')
start = sys.stdin.readline()
num = random.randint(1, 3)
while true:
    print(num)
    a = input()
    i = int(a)
    if i == num:
        print('+ 1 point')
        pass
    elif i < num:
        print('game over')
        break
    elif i > num:
        print('game over')
        break
    



