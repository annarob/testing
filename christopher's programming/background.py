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

