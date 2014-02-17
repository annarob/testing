import sys
import random
num = random.randint(1, 10)
while True:
    float(num)
    print('Guess a number between 1 and 10.')
    G = sys.stdin.readline()
    int(G)
    if G == num:
       print('you win')
    

