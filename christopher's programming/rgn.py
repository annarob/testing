from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    pass
for x in range(1, 100):
    random_rectangle(400, 400, 'green')
    random_rectangle(400, 400, 'red')
    random_rectangle(400, 400, 'blue')
    random_rectangle(400, 400, 'orange')
    random_rectangle(400, 400, 'yellow')
    random_rectangle(400, 400, 'pink')
    random_rectangle(400, 400, 'purple')
    random_rectangle(400, 400, 'violet')
    random_rectangle(400, 400, 'magenta')
    random_rectangle(400, 400, 'cyan')
    random_rectangle(400, 400, '#ffd800')
    pass
canvas.create_text(190, 150, text='Robot funland!!!',
font=('Helvitica',50))
robot4 = canvas.create_rectangle(100, 110, 100, 120)
robot1 = canvas.create_rectangle(500, 500, 480, 480,fill='black')
robot2 = canvas.create_rectangle(100, 100, 105, 105,fill='black')
robot3 = canvas.create_rectangle(95, 90, 105, 110)
def moverobot2(event):
    canvas.move(robot2, 2, 0)
    canvas.move(robot3, 2, 0)
    canvas.move(robot4, 2, 0)
canvas.bind_all('<KeyPress-1>', moverobot2)
def moverobot1(event):
    canvas.move(robot2, -2, 0)
    canvas.move(robot3, -2, 0)
    canvas.move(robot4, -2, 0)
canvas.bind_all('<KeyPress-2>', moverobot1)
def moverobot3(event):
    canvas.move(robot2, 0, -2)
    canvas.move(robot3, 0, -2)
    canvas.move(robot4, 0, -2)
canvas.bind_all('<KeyPress-3>', moverobot3)
def moverobot4(event):
    canvas.move(robot2, 0, 2)
    canvas.move(robot3, 0, 2)
    canvas.move(robot4, 0, 2)
canvas.bind_all('<KeyPress-4>', moverobot4)

for x in range(1, 200):
    canvas.move(robot1, -2, 0)
    tk.update()
    time.sleep(0.05)
    pass
for x in range(1, 200):
    canvas.move(robot1, 0, -2)
    tk.update()
    time.sleep(0.05)
    pass
for x in range(1, 200):
    canvas.move(robot1, 2, 0)
    tk.update()
    time.sleep(0.05)
    pass
for x in range(1, 200):
        canvas.move(robot1, 0, 2)
        tk.update()
        time.sleep(0.05)
        pass
time.sleep(1)
canvas.create_text(190, 100, text='game over.',
font=('Helvitica',50))
    

