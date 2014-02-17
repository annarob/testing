from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=800)
canvas.pack()
tk.title('First Flight')
import random
import time
canvas.create_rectangle(0, 0, 1000, 800, fill='orange')
c2 = colorchooser.askcolor()
b = canvas.create_rectangle(95, 90, 105, 110, fill=c2[1])
a = canvas.create_rectangle(100, 100, 105, 105, fill='black')
c = canvas.create_line(102, 90, 102, 80)
d = canvas.create_line(107, 75, 97,  80)
e = canvas.create_line(107, 80, 97, 75)
f = canvas.create_rectangle(0, 115, 110, 800, fill='brown')
canvas.create_oval(950, 0, 1000, 50, fill='yellow')
def moverobot3(event):
    canvas.move(a, 4, 0)
    canvas.move(b, 4, 0)
    canvas.move(c, 4, 0)
    canvas.move(d, 4, 0)
    canvas.move(e, 4, 0)
canvas.bind_all('<KeyPress-Return>', moverobot3)
for x in range(1, 267):
    canvas.move(a, 0, 3)
    canvas.move(b, 0, 3)
    canvas.move(c, 0, 3)
    canvas.move(d, 0, 3)
    canvas.move(e, 0, 3)
    tk.update()
    time.sleep(0.05)
    pass
canvas.create_text(100, 100, text='Game Over', font=('Times New Roman',45))
