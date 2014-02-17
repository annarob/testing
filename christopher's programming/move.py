from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
def movetriangle(event):
    if event.keysym == 'Left':
        canvas.move(1, -10, 0)
        pass
    
