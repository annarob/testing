from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, height=450, width=450)
canvas.pack()
tk.title('Hop World')
hp = canvas.create_arc(5, 445, 15, 435, extent=359, style=ARC,)
def hop(event):
    for x in range(1, 25):
        canvas.move(hp, 1, -3)
        time.sleep(0.02)
        tk.update()
        for y in range(1, 25):
            coords2 = (y)
    for x in range(1, 25):
        canvas.move(hp, 1, 3)
        time.sleep(0.02)
        tk.update()
canvas.bind_all('<KeyPress-Return>',hop)
for x in range(1, 5):
    for x in range(1, 225):
        canvas.move(hp, 2, 0)
        time.sleep(0.02)
        tk.update()
        for x in range(1, 500):
            coords1 = (x)
    canvas.move(hp, -500, 0)

