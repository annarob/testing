#Python is awesome!
print('Welcome to python Adventure 1.1.0')
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=800)
canvas.pack()
tk.title('Escape Speed')
import random
import time
global fuel
fuel = 0
canvas.create_rectangle(0, 0, 1000, 800, fill='orange')
c2 = colorchooser.askcolor()
b = canvas.create_text(95, 90, text='<py>',font=('Helvetica', 50), fill=c2[1])
canvas.create_rectangle(0, 800, 1000, 500, fill='brown')
canvas.create_rectangle(500, 0, 1000, 400, fill ='brown')
canvas.create_oval(950, 0, 1000, 50, fill='yellow')
def moverobot3(event):
    global fuel
    fuel = (x+7)
    canvas.move(b, 0, -7)
canvas.bind_all('<KeyPress-Return>', moverobot3)
points = canvas.create_text(200, 50, text='PYTHON!' , font=('papyrus',78))
global x
global y
y = 0
for q in range(1, 10):
    PTS = (q)
    points = canvas.create_text(200, 120, text='Level ' + (str(PTS)) + '/10' , font=('papyrus',78))
    for x in range(1, 247):
        fuel = (x)
        y = (x)
        score = (x)
        dscore = canvas.create_text(200, 200, text='==' + (str(score)) + '==' , font=('papyrus',78))
        canvas.move(b, 4, 4)
        tk.update()
        time.sleep(0.05)
        canvas.move(dscore, 10000, 10000)
        if fuel == 180:
            canvas.create_text(300, 300, text='YOU LOSE!', font=('cracked',78), fill='red')
            time.sleep(9999)
        if fuel < 375 and y >=500:
            canvas.create_text(300, 300, text='YOU LOSE!', font=('cracked',78), fill='red')
            time.sleep(9999)
        pass
    canvas.move(b, -1000, 4)
canvas.create_text(300, 300, text='You Win!', font=('papyrus',78), fill='brown')



