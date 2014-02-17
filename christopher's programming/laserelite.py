print('welcome to laser elite. © copyright 2013 cbroc inc.')
import time
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.color(0, 0, 1)
t.up()
t.backward(450)
a = turtle.Turtle()
a.color(0, 0.5, 0)
a.up()
a.forward(450)
a.right(180)
def Q():
    a.color(1, 0, 0)

    print('player 1 wins!')
    pass
def P():
    t.color(1, 0, 0)
    print('player 2 wins!')
    pass
def shop():
    print('type meds to buy meds')
    print('type shield to buy shield')
    pass
meds = ('buy sucsessful. type z() if player 1 or m() if player 2 to heal')
shield = ('buy sucsessful. type a() if player 1 or l() if player 2 to activate shield')
def z():
    t.color(0, 0.5, 0)
    pass
def m():
    a.color(0, 0.5, 0)
    pass
def a():
    time.sleep(1)
    pass
def l():
    time.sleep(1)
    pass

    
    
    
    

