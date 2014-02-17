from tkinter import *
import sys
import random
tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
version = 1.2
tk.title('Earth World %s' % version)
if version == 1.2 :
    print(version)
def tree(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill='green')
    x3 = x1 + 10
    x4 = x2 - 10
    y4 = y2 + 15
    canvas.create_rectangle(x3, y1, x4, y4, fill='brown')
    canvas.create_rectangle(x1, y1, x2, y2, fill='green')
def cave():
    xx = random.randrange(500)
    yy = random.randrange(30)
    xxx = xx + 100
    yyy = yy + 100
    d = canvas.create_rectangle(xx, yy, xxx, yyy, fill='grey')
tree(50, 25, 80, 45)
t = random.randrange(1000)
v = t + 30
tree(t, 25, v, 45)
a = random.randrange(1000)
b = a + 30
tree(a, 25, b, 45)
c = random.randrange(1000)
d = c + 30
tree(c, 25, d, 45)
e = random.randrange(1000)
f = e + 30
tree(e, 25, f, 45)
canvas.create_rectangle(0, 80, 1000, 1000, fill='black')
robot4 = canvas.create_rectangle(100, 110, 100, 120, fill='brown')
robot3 = canvas.create_rectangle(95, 90, 105, 110, fill='brown')
robot2 = canvas.create_rectangle(100, 100, 105, 105,fill='green')
canvas.create_rectangle(0, 50, 1005, 80, fill='green')
gold = canvas.create_polygon(900, 900, 870, 930, 900, 960, 930, 930, fill='#ffd800')
title1 = canvas.create_rectangle(0, 0, 1000, 1000, fill='green')
title2 = canvas.create_text(400, 400,text='Earthworld  %s' % version, font='Copperplate')
title3 = canvas.create_text(400, 500,text='press RETURN to play', font='Copperplate')
canvas.move(robot2, 0, -70)
canvas.move(robot3, 0, -70)
canvas.move(robot4, 0, -70)
def move1(event):
    canvas.move(robot2, 3, 0)
    canvas.move(robot3, 3, 0)
    canvas.move(robot4, 3, 0)
canvas.bind_all('<KeyPress-Right>', move1)
def move2(event):
    canvas.move(robot2, -3, 0)
    canvas.move(robot3, -3, 0)
    canvas.move(robot4, -3, 0)
canvas.bind_all('<KeyPress-Left>', move2)
def move3(event):
    canvas.move(robot2, 0, 1)
    canvas.move(robot3, 0, 1)
    canvas.move(robot4, 0, 1)
canvas.bind_all('<KeyPress-Down>', move3)
def move4(event):
    canvas.move(robot2, 0, -1)
    canvas.move(robot3, 0, -1)
    canvas.move(robot4, 0, -1)
canvas.bind_all('<KeyPress-Up>', move4)
def usepick(event):
    score = (random.randrange(10000))
    score2 = (str(score))
    print('money:')
    print(score2)
    canvas.move(gold, 3456, 0)
canvas.bind_all('<KeyPress-Tab>',usepick)
def strt(event):
    canvas.move(title1, 0, 10000)
    canvas.move(title2, 0, 10000)
    canvas.move(title3, 0, 10000)
canvas.bind_all('<KeyPress-Return>', strt)


    
