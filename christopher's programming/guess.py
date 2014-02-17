import random
num = random.randrange(100000)
for x in range(1, 150):
    print('Guess a number between 1 and 100000')
    guess = input()
    guess2 = (int(guess))
    if guess2 == num:
        print('you win')
    if guess2 > num:
        print('too high')
    if guess2 < num:
        print('too low.')
    
