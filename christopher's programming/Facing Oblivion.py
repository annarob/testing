#Facing Oblivion
import random
import time
import pickle
#Creating player
class player():
    def Player():
        #chosing character loop
        global ChosenCharacter
        global NPC
        while True:
            print('Choose your character:')
            print('Io, Prometheus')
            typed = input()
            response = (str(typed))
            if response == 'io':
                ChosenCharacter = 'Io'
                print('Chosen ' + ChosenCharacter)
                NPC = 'Prometheus'
                break
            if response == 'prometheus':
                ChosenCharacter = 'Prometheus'
                print('Chosen ' + ChosenCharacter)
                NPC = 'Io'
                break
    def Spawn():
        possible = ['desert', 'rainforest', 'high plateau', 'forest']
        global biome
        biome = random.choice(possible)
        print('You are in a ' + biome + '.')
#Creating Village
class house():
    def House():
        print('You entered a house.')
        possible = ['villager', 'priest', 'farmer', 'scribe']
        print('You see a ' + (random.choice(possible)) + ' inside.')
        print('Type speak to talk to them.')
        print('Type exit to leave the house.')
        typed = input()
        response = (str(typed))
        if response == 'speak':
            possible = ['Bob.', 'George.', 'Emma.', 'Chloe.']
            print('Nice to meet you ' + ChosenCharacter)
            print('My name is ' + (random.choice(possible)))
            Status = random.randint(1, 6)
            if Status == 1:
                print('I have somthing for you. Take it.')
                print('Obtained Warp crystal!')
                print('Press enter to use it.')
                typed = input()
                sanctuary.Sanctuary()
            if Status != 1:
                street.Street()
        if response != 'speak':
            street.Street()
class street():
    def Street():
        print('You are in the streets.')
        print('Type forward, right, left')
        typed = input()
        response = (str(typed))
        if response == 'forward':
            house.House()
        if response == 'left':
            house.House()
        if response == 'right':
            house.House()
class village():
    def Village():
        print('You see a village. Enter it?')
        print('yes, no')
        typed = input()
        response = (str(typed))
        if response == 'yes':
            street.Street()
class sanctuary():
    def Sanctuary():
        print('You warped into the sanctuary.')
        print('<' + NPC + '> ' + ChosenCharacter + '! finally, you arrived.')
        print('Let\'s begin.')
        print('Together, we have infinte amounts of physic power.')
        print('But apart, our physic powers are worthless.')
        print('Only we can stop oblivion, ' + ChosenCharacter + '.')
        print('*BAM*')
        time.sleep(1)
        print('What was that?')
        print('<' + NPC + '> ' + ChosenCharacter + ', I want you to have this.')
        print('*BAM*')
        print('<' + NPC + '> ' + ChosenCharacter + ',go on without me, I promise, we will find eachother again.')
        print('RUN, run as fast as you can! Get away as soon as possible, and we will see each other again! RUN!')
        print('Obtained Summon Meteorite!')
        print('Press enter to use it.')
        typed = input()
        print('Meteorite summoned.')
        print('*EXPLOSION*')
        print('')
        meteorite.Meteorite()
    def warehouse():
        print('Who is there?')
        print('Ahh, it\'s ' + ChosenCharacter + '.')
        print('Your friend put up a fight, but now ' + NPC + ' is in one of my dungeons.')
        print('You will soon join them')
        print('Goodbye, ' + ChosenCharacter + '.')
        print('I will make myself a god, and send this world into oblivion.')
        print('Press enter to continue.')
        typed = input()
    def dungeon():
        while True:
            print('You are in the dark.')
            print('Type forward, right, left')
            typed = input()
            response = (str(typed))
            if response == 'forward':
                possible = random.randrange(3)
                if possible == 1:
                    print('Obtained torch! press enter to use it.')
                    typed = input()
                    Dungeon.LitDungeon()
                    break
            if response == 'left':
                possible = random.randrange(3)
                if possible == 1:
                    print('Obtained torch! press enter to use it.')
                    typed = input()
                    Dungeon.LitDungeon()
                    break
            if response == 'right':
                possible = random.randrange(3)
                if possible == 1:
                    print('Obtained torch! press enter to use it.')
                    typed = input()
                    Dungeon.LitDungeon()
                    break
class Dungeon():
    def LitDungeon():
        while True:
            print('You are in a dungeon.')
            print('Type forward, right, left')
            typed = input()
            response = (str(typed))
            if response == 'forward':
                possible = random.randrange(8)
                if possible == 1:
                    print('<' + NPC + '>' + ChosenCharacter + '? It\'s you!')
                    print('Press enter to continue.')
                    typed = input()
                    print('Hold my hand')
                    print('Press enter to continue.')
                    typed = input()
            if response == 'left':
                possible = random.randrange(8)
                if possible == 1:
                    print('<' + NPC + '>' + ChosenCharacter + '? It\'s you!')
                    print('Press enter to continue.')
                    typed = input()
                    print('Hold my hand')
                    print('Press enter to continue.')
                    typed = input()
            if response == 'right':
                possible = random.randrange(8)
                if possible == 1:
                    print('<' + NPC + '>' + ChosenCharacter + '? It\'s you!')
                    print('Press enter to continue.')
                    typed = input()
                    print('Hold my hand')
                    print('Press enter to continue.')
                    typed = input()
class meteorite():
    def Meteorite():
        print('You wake up on a stray asteroid, heading through the cosmos.')
        print('You see a small glimmer on the ground ahead of you.')
        print('Pick it up?')
        print('Yes, no')
        typed = input()
        response = (str(typed))
        if response == 'yes':
            print('Obtained Lunar Compass')
            print('press enter to use it.')
            typed = input()
            print('Coordinates obtained. Press enter to set course.')
            typed = input()
            print('Setting course...')
            time.sleep(5)
            sanctuary.warehouse()
            sanctuary.dungeon()
#Main game loop
while True:
    player.Player()
    player.Spawn()
    village.Village()
                

            

    
