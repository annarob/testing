from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=800)
canvas.pack()
tk.title('Autumn Fall')
import random
import time
canvas.create_rectangle(0, 0, 1000, 800, fill='orange')
c2 = colorchooser.askcolor()
b = canvas.create_rectangle(95, 90, 105, 110, fill=c2[1])
a = canvas.create_rectangle(100, 100, 105, 105,fill='black')
c = canvas.create_line(102, 90, 102, 80)
d = canvas.create_line(107, 75, 97,  80)
e = canvas.create_line(107, 80, 97, 75)
f = canvas.create_rectangle(0, 800, 1000, 775, fill='brown')
canvas.create_oval(950, 0, 1000, 50, fill='yellow')
def moverobot3(event):
    canvas.move(a, 0, -7)
    canvas.move(b, 0, -7)
    canvas.move(c, 0, -7)
    canvas.move(d, 0, -7)
    canvas.move(e, 0, -7)
canvas.bind_all('<KeyPress-Return>', moverobot3)
for x in range(1, 3):
    for x in range(1, 247):
        canvas.move(a, 4, 4)
        canvas.move(b, 4, 4)
        canvas.move(c, 4, 4)
        canvas.move(d, 4, 4)
        canvas.move(e, 4, 4)
        tk.update()
        time.sleep(0.05)
        pass
    canvas.move(a, -1000, 4)
    canvas.move(b, -1000, 4)
    canvas.move(c, -1000, 4)
    canvas.move(d, -1000, 4)
    canvas.move(e, -1000, 4)
canvas.create_text(300, 300, text='You Win!', font=('papyrus',78), fill='brown')


