print('Cave Kingdom news:')
print('you can now create objects and light up your path with a light!')
print('Cave Kingdom™ v2 has been realeased!')
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1500, height=1000)
canvas.pack()
import random
import time
canvas.create_rectangle(0, 0, 1500, 1000, fill='black')
canvas.create_oval(20, 20, 80, 80, fill='grey')
canvas.create_oval(60, 60, 100, 100, outline='grey', fill='grey')
def randomcave(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_oval(x1, y1, x2, y2, outline='grey', fill='grey')
tk.title('Cave Kingdom™')
print('it\'s as easy as π!')  
for x in range(1, 5):
    randomcave(45, 45)
for x in range(1, 5):
    randomcave(90, 90)
for x in range(1, 5):
    randomcave(135, 135)
for x in range(1, 5):
    randomcave(180, 180)
for x in range(1, 5):
    randomcave(500, 500)
for x in range(1, 5):
    randomcave(500, 500)
for x in range(1, 5):
    randomcave(500, 500)
for x in range(1, 5):
    randomcave(500, 500)
for x in range(1, 5):
    randomcave(45, 45)
for x in range(1, 5):
    randomcave(90, 90)
for x in range(1, 5):
    randomcave(135, 135)
for x in range(1, 5):
    randomcave(180, 180)
for x in range(1, 5):
    randomcave(500, 500)
for x in range(1, 5):
    randomcave(500, 500)
for x in range(1, 5):
    randomcave(500, 500)
robot9 = canvas.create_oval(90, 85, 110, 115,outline='yellow', fill='yellow')
robot4 = canvas.create_rectangle(100, 110, 100, 120)
robot2 = canvas.create_rectangle(100, 100, 105, 105,fill='#ffd800')
robot3 = canvas.create_rectangle(95, 90, 105, 110)
robot8 = canvas.create_oval(90, 85, 110, 115,outline='yellow', fill='yellow')
def moverobot2(event):
    canvas.move(robot2, 5, 0)
    canvas.move(robot3, 5, 0)
    canvas.move(robot4, 5, 0)
    canvas.move(robot9, 5, 0)
canvas.bind_all('<KeyPress-1>', moverobot2)
def moverobot1(event):
    canvas.move(robot2, -5, 0)
    canvas.move(robot3, -5, 0)
    canvas.move(robot4, -5, 0)
    canvas.move(robot9, -5, 0)
canvas.bind_all('<KeyPress-2>', moverobot1)
def moverobot3(event):
    canvas.move(robot2, 0, -5)
    canvas.move(robot3, 0, -5)
    canvas.move(robot4, 0, -5)
    canvas.move(robot9, 0, -5)
canvas.bind_all('<KeyPress-3>', moverobot3)
def moverobot4(event):
    canvas.move(robot2, 0, 5)
    canvas.move(robot3, 0, 5)
    canvas.move(robot4, 0, 5)
    canvas.move(robot9, 0, 5)
canvas.bind_all('<KeyPress-4>', moverobot4)
robot5 = canvas.create_rectangle(100, 110, 100, 120)
robot6 = canvas.create_rectangle(100, 100, 105, 105,fill='orange')
robot7 = canvas.create_rectangle(95, 90, 105, 110)
def moverobot3(event):
    canvas.move(robot5, 3, 0)
    canvas.move(robot6, 3, 0)
    canvas.move(robot7, 3, 0)
    canvas.move(robot8, 3, 0)
canvas.bind_all('<KeyPress-5>', moverobot3)
def moverobot4(event):
    canvas.move(robot5, -3, 0)
    canvas.move(robot6, -3, 0)
    canvas.move(robot7, -3, 0)
    canvas.move(robot8, -3, 0)
canvas.bind_all('<KeyPress-6>', moverobot4)
def moverobot5(event):
    canvas.move(robot5, 0, -3)
    canvas.move(robot6, 0, -3)
    canvas.move(robot7, 0, -3)
    canvas.move(robot8, 0, -3)
canvas.bind_all('<KeyPress-7>', moverobot5)
def moverobot6(event):
    canvas.move(robot5, 0, 3)
    canvas.move(robot6, 0, 3)
    canvas.move(robot7, 0, 3)
    canvas.move(robot8, 0, 3)
canvas.bind_all('<KeyPress-8>', moverobot6)
def improved_engines(self):
    pass
def π():
    print('created by Good Graphix Games. Special thanks to many contributeurs. copyright © 2013 Good Graphix Games. All rights reserved.')
def buildblock1(event):
    x = random.randrange(600)
    y = random.randrange(600)
    xx = x + 60
    yy = y + 60
    canvas.create_rectangle(x, y, xx, yy, outline='brown', fill='brown')
canvas.bind_all('<KeyPress-Tab>',buildblock1)
def buildblock2(event):
    x = random.randrange(800)
    y = random.randrange(800)
    xx = x + 60
    yy = y + 60
    canvas.create_rectangle(x, y, xx, yy, outline='orange', fill='orange')
canvas.bind_all('<KeyPress-Return>',buildblock2)   



