import time
import random
print("Welcome to Labrinth.")
print('type left or right to get the treasure.')
print('Press ENTER to go into the labrinth.')
typed = input()
Message = 'Leave this place!'
room1 = ['Written on the wall: The ghosts write on the walls. We are lost here. Alone. In the dark.', 'left']
room2 = ['Written on the wall: We are lost here all alone. The trumpet blows west toward god.', 'right']
room3 = ['Written on the wall: How many miles can you run in the dark, what choice did you make on the path to light?', 'right']
room4 = ['Written on the wall: The wind of the north is blowing west.Onward on our way.', 'left']
room5 = ['Written on the wall: I thrive in the dark, in the dark I thrive. The guess is yours, dead or alive.', 'left']
room6 = ['Written on the wall: Abandoned by my love so dear. We reside here eternally.', 'left']
room7 = ['Written on the wall: I abandoned my love. I then later failed. That is what I ethically deserve.', 'right']
def FindRoom():
    possible = [room1, room2, room3, room4, room5, room6, room7]
    global chosen
    chosen = random.choice(possible)
    print(chosen[0])
def lost():
    FindRoom()
    typed = input()
    response = str(typed)
    print('You got lost in the labrinth. You are now a')
    print('ghost. Type a message on the walls for future travellers.')
    typed = input()
    response = str(typed)
    global Message
    Message = (response)
    begin.start()
class begin():
    def start():
        print('Written on the wall: ' + Message + '.')
        print('Written on the wall: The ghosts write on the walls. Turn right.')
        typed = input()
        response = str(typed)
        if response == 'right':
            medium.Medium()
            pass
        if response != 'right':
            lost()
            pass
class medium():
    def Medium():
        for x in range(1, 30):
            FindRoom()
            typed = input()
            response = str(typed)
            if response == chosen[1]:
                print('Gone ' + chosen[1] + '.')
            if response != chosen[1]:
                print('Gone ' + chosen[1] + '.')
                lost()
        end.End()
class end():
    def End():
        print('You are near the treasure room, just one more turn.')
        print('The end is near, traveller. make the choice.')
        print('Make the right choice.')
        typed = input()
        response = str(typed)
        if response == 'left':
            print('You found the treasure!')
            time.sleep(55555)
        if response != chosen[1]:
            lost()
begin.start()
            


      
