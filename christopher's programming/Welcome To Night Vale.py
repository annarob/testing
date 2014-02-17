import time
import random
import pickle
class ForTechMus():
    def House():
        print('You have entered the Museum of Forbidden Technologies.')
        Obj1 = ['bookcase', 'Cthulu Statue', 'bloodstone', 'shelf']
        Obj2 = ['a cat.', 'a dog.', 'The Faceless Woman Who Secretely lives in your home.', 'Old woman Jose.', 'John Peters, you know, the farmer.']
        ChObj1 = random.choice(Obj1)
        ChObj2 = random.choice(Obj2)
        print('There is a ' + ChObj1 + ' in the corner. You see ' + ChObj2)
        print('You see a time machine. Type \'enter\' to enter the time machine, and type \'exit\' to leave.')
        typed = input()
        response = (str(typed))
        if response == 'exit':
            Street1.Move()
        if response != 'exit':
            print('You enter the time machine. The doors close and you appear in the streets. It is a lazy day in Night Vale.')
            print('Your heart decides to take the day off, and you fall dead in the streets.')
            print('Wait 5 minutes for the lazy day to end, so you can return to work.')
            time.sleep(300)
            global level
            level = '2!'
            print('You have Acheived level ' + level)
            Street2.Move()
class library():
    def Library():
        print('You have entered the library.')
        Obj1 = ['bookcase', 'Cthulu Statue', 'bloodstone', 'shelf']
        Obj2 = ['a cat.', 'a dog.', 'The Faceless Woman Who Secretely lives in your home.', 'Old woman Jose.', 'John Peters, you know, the farmer.']
        ChObj1 = random.choice(Obj1)
        ChObj2 = random.choice(Obj2)
        print('There is a ' + ChObj1 + ' in the corner. You see ' + ChObj2)
        print('type \'look\' to explore')
        typed = input()
        response = (str(typed))
        if response == 'look':
            print('You see a ton of librarians.')
            print('They begin to chase you.')
            print('Type \'run\' to run away, and type \'hide\' to hide from them.')
            typed = input()
            response = (str(typed))
            if response == 'hide':
                print('While hiding, you find a way out.')
                print('You Escaped The library!')
                global level
                level = '1!'
                print('You have Acheived level ' + level)
                Street2.Move()
            if response != 'hide':
                print('The librarians are fast, and quickly catch you.')
                print('The librarians gorge on your remains.')
                print('You are dead.')
                radioStation.Start()
class house():
    def House():
        Obj1 = ['bookcase', 'Cthulu Statue', 'bloodstone', 'shelf']
        Obj2 = ['a cat.', 'a dog.', 'The Faceless Woman Who Secretely lives in your home.', 'Old woman Jose.', 'John Peters, you know, the farmer.']
        ChObj1 = random.choice(Obj1)
        ChObj2 = random.choice(Obj2)
        print('There is a ' + ChObj1 + ' in the corner. You see ' + ChObj2)
        print('type \'exit\' to leave')
        typed = input()
        response = (str(typed))
        if response == 'exit':
            print('You are in the streets.')
            Street1.Move()
def Intro():
  Intro = ['The trees are missing. Hopefully they will be back soon.', 'The Houses are ablaze.', 'All hail the glow cloud.']
  ChosenIntro = random.choice(Intro)
  print(ChosenIntro + ' Welcome, dear player, to Night Vale.')
  print('Press ENTER to continue.')
  response = input()
class radioStation():
    def Start():
        print('You are in a radio station.')
        print('Type \'look\' to explore the room.')
        print('Type \'exit\' to leave.')
        while True:
            typed = input()
            response = (str(typed))
            if response == 'look':
                print('There is an abandoned Radio Booth in the corner. Inside, there is  a small tape casette.')
                print('Type \'exit\' to leave.')
            if response == 'exit':
                print('You are in the streets.')
                Street1.Move()
                break
class Street1():
    def Move():
        print('type forward to go into the house in front of you.')
        print('type left to go left, and right to go right.')
        typed = input()
        response = (str(typed)) 
        if response == 'forward':
            house.House()
        if response == 'left':
            library.Library()
            
class Street2():
    def Move():
        print('type forward to go into the dog park.')
        print('type left to go left, and right to go right.')
        typed = input()
        response = (str(typed)) 
        if response == 'forward':
            house.House()
        if response == 'left':
            house.House()
        if response == 'right':
            ForTechMus.House()
Intro()
radioStation.Start()

            

    
            
        
