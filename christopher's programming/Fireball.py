from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
Background = canvas.create_rectangle(0, 0, 500, 500, fill='grey')
Area = canvas.create_rectangle(215, 300, 270, 240, fill='cyan')
a = canvas.create_rectangle(250, 250, 255, 255, fill='green')
canvas.move(a, 10, 0)
Coords1 = 1
Coords2 = 1
global health
health = 1
canvas.create_oval(10, 10, 30, 30, fill='green')
canvas.create_oval(40, 10, 60, 30, fill='green')
def Move1(event):
    global Coords1
    if Coords1 != 1:
        canvas.move(a, 40, 0)
        Coords1 = 1
canvas.bind_all('<KeyPress-Right>', Move1)
def Move2(event):
    global Coords1
    if Coords1 != 2:
        canvas.move(a, -40, 0)
        Coords1 = 2
canvas.bind_all('<KeyPress-Left>', Move2)
def Move3(event):
    global Coords2
    if Coords2 != 2:
        canvas.move(a, 0, 40)
        Coords2 = 2
canvas.bind_all('<KeyPress-Down>', Move3)
def Move4(event):
    global Coords2
    if Coords2 != 1:
        canvas.move(a, 0, -40)
        Coords2 = 1
canvas.bind_all('<KeyPress-Up>', Move4)

        

            






