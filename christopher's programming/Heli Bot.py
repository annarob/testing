from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=800)
canvas.pack()
tk.title('Heli Bot')
import random
import time
def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    pass
for x in range(1, 1000):
    random_rectangle(4000, 4000, 'green')
    random_rectangle(4000, 4000, 'red')
    random_rectangle(4000, 4000, 'blue')
    random_rectangle(4000, 4000, 'orange')
    random_rectangle(4000, 4000, 'yellow')
    random_rectangle(4000, 4000, 'pink')
    random_rectangle(4000, 4000, 'purple')
    random_rectangle(4000, 4000, 'violet')
    random_rectangle(4000, 4000, 'magenta')
    random_rectangle(4000, 4000, 'cyan')
    random_rectangle(4000, 4000, '#ffd800')
    pass
a = canvas.create_rectangle(100, 100, 105, 105)
b = canvas.create_rectangle(95, 90, 105, 110)
c = canvas.create_line(102, 90, 102, 80)
d = canvas.create_line(107, 75, 97,  80)
e = canvas.create_line(107, 80, 97, 75)
canvas.create_rectangle(980, 780, 1000, 800, fill='black')
canvas.create_rectangle(980, 730, 1000, 750, fill='black')
canvas.create_rectangle(980, 680, 1000, 700, fill='black')
canvas.create_rectangle(980, 630, 1000, 650, fill='black')
canvas.create_rectangle(980, 580, 1000, 600, fill='black')
canvas.create_rectangle(980, 530, 1000, 550, fill='black')
canvas.create_rectangle(980, 480, 1000, 500, fill='black')
canvas.create_rectangle(980, 430, 1000, 450, fill='black')
canvas.create_rectangle(980, 380, 1000, 400, fill='black')
canvas.create_rectangle(980, 330, 1000, 350, fill='black')
canvas.create_rectangle(980, 280, 1000, 300, fill='black')
canvas.create_rectangle(980, 230, 1000, 250, fill='black')
canvas.create_rectangle(980, 180, 1000, 200, fill='black')
canvas.create_rectangle(980, 130, 1000, 150, fill='black')
canvas.create_rectangle(980, 80, 1000, 100, fill='black')
canvas.create_rectangle(980, 30, 1000, 50, fill='black')
canvas.create_rectangle(680, 380, 700, 400, fill='black')
canvas.create_rectangle(680, 680, 700, 700, fill='black')
canvas.create_rectangle(680, 630, 700, 650, fill='black')
canvas.create_rectangle(680, 580, 700, 600, fill='black')
canvas.create_rectangle(680, 530, 700, 550, fill='black')
canvas.create_rectangle(380, 0, 700, 20, fill='black')
canvas.create_rectangle(380, 30, 400, 50, fill='black')
canvas.create_rectangle(380, 60, 400, 80, fill='black')
canvas.create_rectangle(380, 90, 400, 110, fill='black')
canvas.create_rectangle(380, 140, 400, 160, fill='black')
canvas.create_rectangle(380, 170, 400, 190, fill='black')
canvas.create_rectangle(380, 200, 400, 220, fill='black')
def moverobot3(event):
    canvas.move(a, 0, -2)
    canvas.move(b, 0, -2)
    canvas.move(c, 0, -2)
    canvas.move(d, 0, -2)
    canvas.move(e, 0, -2)
canvas.bind_all('<KeyPress-1>', moverobot3)
def moverobot4(event):
    canvas.move(a, 0, 8)
    canvas.move(b, 0, 8)
    canvas.move(c, 0, 8)
    canvas.move(d, 0, 8)
    canvas.move(e, 0, 8)
canvas.bind_all('<KeyPress-2>', moverobot4)
time.sleep(0.5)
for x in range(1, 2000000):
    canvas.move(a, 3, 0)
    canvas.move(b, 3, 0)
    canvas.move(c, 3, 0)
    canvas.move(d, 3, 0)
    canvas.move(e, 3, 0)
    canvas.move(a, 0, 1)
    canvas.move(b, 0, 1)
    canvas.move(c, 0, 1)
    canvas.move(d, 0, 1)
    canvas.move(e, 0, 1)
    tk.update()
    time.sleep(0.05)
    pass


   



























    
