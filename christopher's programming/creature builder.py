from tkinter import *
import sys
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
circle = 1
square = 2
claw = 3
basicleg = 4
tk.title('Creature Builder™')
def body(shape):
    if shape == circle:
        c = colorchooser.askcolor()
        canvas.create_oval(200, 200, 300, 300, fill=c[1])
    if shape == square:
        c = colorchooser.askcolor()

        canvas.create_rectangle(200, 200, 300, 300, fill=c[1])
def leg(legtype):
    if legtype == claw:
        c = colorchooser.askcolor()
        canvas.create_line(250, 250, 200, 200, fill=c[1])
        canvas.create_oval(210, 100, 200, 220, fill=c[1])
        canvas.create_line(250, 250, 400, 100, fill=c[1])
        canvas.create_oval(220, 100, 440, 110, fill=c[1])
    if legtype == basicleg:
        c = colorchooser.askcolor()
        canvas.create_line(250, 250, 200, 200, fill=c[1])
        canvas.create_line(250, 250, 400, 100, fill=c[1])
def head():
    canvas.create_line(250, 250, 200, 200, fill=c[1])
    canvas.create_oval
    
        
        
    
