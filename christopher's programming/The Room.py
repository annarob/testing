import time
import random
import pickle
global WeaponRating
print('Welcome to THE ROOM.')
class room():
    def treasure():
        Possible = ['sword', 'diamond', 'gold coin', 'Granite Shield', 'ruby', 'sapphire', 'gold medallion', 'silver chain', 'steel sword', 'crown', 'silver coin', 'copper coin']
        loot = random.choice(Possible)
        print('you found a ' + loot)
    def monster():
        Possible = ['goblin', 'skeleton', 'zombie', 'witch', 'Giant spider', 'necromancer']
        monster = random.choice(Possible)
        print('There is a ' + monster +' in the room.')
        Status = ['beat', 'got beaten by']
        bstatus = random.choice(Status)
        print('You ' + bstatus + ' the ' + monster)
    def object1():
        Possible = ['bookcases.', 'couldrons.', 'cobwebs.', 'bones.', 'ashes.', 'corpses.', 'potions.']
        Object = random.choice(Possible)
        print('The room is filled with ' + Object)
    def object2():
        Possible = ['bone', 'Spell Book', 'puddle of blood', 'skull', 'bloody head', 'bloody knife', ' crying baby']
        Object = random.choice(Possible)
        print('There is a ' + Object + ' on the floor.')
    def object3():
        Possible = ['black cat.', 'severed hand.', 'green light.', 'axe.', 'smashed television.', 'candle.', 'broken window.']
        Object = random.choice(Possible)
        print('You see a ' + Object)
for x in range(1, 250):
    print('press enter to continue')
    response = input()
    print('You are in room ' + str(x))
    room.treasure()
    room.monster()
    room.object1()
    room.object2()
    room.object3()
    

        
        
