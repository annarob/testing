import time
print('Welcome to The Trolling Troll.')
print('Press enter to play.')
typed = input()
response = str(typed)
print('Destroy the troll!')
print('Type in what to do.')
for x in range(1, 6):
    typed = input()
    response = str(typed)
    if response == 'put a rubber ducky in his mouth':
        print('You defeated the troll!')
        print('While leaving, you trip on his corpse and die. GAME OVER.')
        time.sleep(99999)
    if response != 'put a rubber ducky in his mouth':
        print('You can not ' + response + '.')
print('The troll crushed you.')
print('GAME OVER')
copyright()

    
    
