#This is a number game.
import random
print('hello! What is your name?')
name = input()
print('Well, %s, I am thinking of a number between 1 and 20' % name)
print('Take a guess.')
tries = 1
num = random.randint(1, 20)
for x in range(1, 7):
    response = input()
    guess = (int(response))
    if guess == num:
        print('Good Job, '+ name', you guessed my number in' + tries 'guesses!')
        break
    if guess > num:
        print('too high. Try again.')
    if guess < num:
        print('too low. Try again.')
    tries = tries + 1
print('you lose.')
    

