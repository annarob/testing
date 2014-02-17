# there should be a file header comment
from tkinter import *
def fr():
    canvas.create_text(180, 200, text='GOOO!',font=('Cracked', 50,),fill='green')
    pass
import random
tk = Tk()
btn = Button(tk, text="start", command=fr)
btn.pack()
canvas = Canvas(tk, height=400, width=400)
canvas.pack()
tk.title('A Big Green Worm')
canvas.create_text(180, 50, text='A Big Green Worm With',font=('Cracked', 50,),fill='green')
canvas.create_text(180, 120, text='Rolling Eyes',font=('Cracked', 50,),fill='green')
worm = canvas.create_oval(150, 150, 170, 170, fill='green')
worm2 = canvas.create_oval(150, 150, 170, 170, fill='green')
canvas.move(worm2, -10, 0)
worm3 = canvas.create_oval(150, 150, 170, 170, fill='green')
canvas.move(worm3, -20, 0)
def move1(event):
    canvas.move(worm, -2, 0)
    canvas.move(worm2, -2, 0)
    canvas.move(worm3, -2, 0)
canvas.bind_all('<KeyPress-1>', move1)
def move2(event):
    canvas.move(worm, 2, 0)
    canvas.move(worm2, 2, 0)
    canvas.move(worm3, 2, 0)
canvas.bind_all('<KeyPress-2>', move2)
def move3(event):
    canvas.move(worm, 0, -2)
    canvas.move(worm2, 0, -2)
    canvas.move(worm3, 0, -2)
canvas.bind_all('<KeyPress-3>', move3)
def move4(event):
    canvas.move(worm, 0, 2)
    canvas.move(worm2, 0, 2)
    canvas.move(worm3, 0, 2)
canvas.bind_all('<KeyPress-4>', move4)
def spitslime(event):
    x1 = random.randrange(400)
    y1 = random.randrange(400)
    x2 = x1 + 10
    y2 = y1 + 10
    canvas.create_oval(x1, y1, x2, y2, fill='green')
canvas.bind_all('<KeyPress-5>', spitslime)

    
