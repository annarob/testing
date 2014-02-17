from tkinter import *
import time
import random
tk = Tk()
canvas = Canvas(tk, width=1800, height=1100)
canvas.pack()
background = canvas.create_rectangle(0, 0, 1800, 1100, fill='grey')
tk.title('Scavenger')
scsprite = canvas.create_oval(480, 480, 500, 500, fill='blue')
pry1 = canvas.create_oval(480, 480, 500, 500, fill='green')
pry2 = canvas.create_oval(480, 480, 500, 500, fill='green')
pry3 = canvas.create_oval(480, 480, 500, 500, fill='green')
prsn1 = canvas.create_oval(480, 480, 500, 500, fill='tan')
dmg = 0
canvas.move(prsn1, 500, 0)
canvas.move(pry1, 300, 0)
canvas.move(pry2, 200, 0)
canvas.move(pry3, 400, 0)
def move1(event):
    canvas.move(scsprite, 1, 0)
canvas.bind_all('<KeyPress-Right>', move1)
def move2(event):
    canvas.move(scsprite, -1, 0)
canvas.bind_all('<KeyPress-Left>', move2)
def move3(event):
    canvas.move(scsprite, 0, -1)
canvas.bind_all('<KeyPress-Up>', move3)
def move4(event):
    canvas.move(scsprite, 0, 1)
canvas.bind_all('<KeyPress-Down>', move4)
for x in range(1, 100):
    time.sleep(0.5)
    dmg = (x)
    print(str(dmg))
    if dmg == 50:
        print('you died.')


