from tkinter import *
import time
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
tk.title('Math Game')
global response
global crctresponse
crctresponse = (4)
gb1 = canvas.create_rectangle(0, 0, 400, 400, fill='red')
gb2 = canvas.create_text(150, 40, text='8 - 4 = ?', font=('Pea Sugar Noodles', 20))
robot4 = canvas.create_rectangle(100, 110, 100, 120)
robot2 = canvas.create_rectangle(100, 100, 105, 105,fill='black')
robot3 = canvas.create_rectangle(95, 90, 105, 110)
canvas.move(robot4, -95, 0)
canvas.move(robot3, -95, 0)
canvas.move(robot2, -95, 0)
ttl1 = canvas.create_rectangle(0, 0, 400, 400, fill='orange')
ttl2 = canvas.create_text(150, 40, text='Press RETURN to play', font=('Pea Sugar Noodles', 20))
def startgame(event):
    canvas.move(ttl1, 500, 0)
    canvas.move(ttl2, 500, 0)
canvas.bind_all('<KeyPress-Return>', startgame)
def respond1(event):
    response = (1)
    if response == crctresponse:
        canvas.move(gb2, 500, 0)
        gb4 = canvas.create_text(150, 40, text='Correct!', font=('Pea Sugar Noodles', 20))
canvas.bind_all('<KeyPress-1>', respond1)
def respond2(event):
    response = (2)
    if response == crctresponse:
        canvas.move(gb2, 500, 0)
        gb4 = canvas.create_text(150, 40, text='Correct!', font=('Pea Sugar Noodles', 20))
canvas.bind_all('<KeyPress-2>', respond2)
def respond3(event):
    response = (3)
    if response == crctresponse:
        canvas.move(gb2, 500, 0)
        gb4 = canvas.create_text(150, 40, text='Correct!', font=('Pea Sugar Noodles', 20))
canvas.bind_all('<KeyPress-3>', respond3)
def respond4(event):
    response = (4)
    if response == crctresponse:
        canvas.move(gb2, 500, 0)
        gb4 = canvas.create_text(150, 40, text='Correct!', font=('Pea Sugar Noodles', 20))
canvas.bind_all('<KeyPress-4>', respond4)

for x in range(1, 200):
    canvas.move(robot4, 1, 0)
    canvas.move(robot3, 1, 0)
    canvas.move(robot2, 1, 0)
    time.sleep(0.05)
    tk.update()
canvas.move(gb2, 500, 0)
gb3 = canvas.create_text(150, 80, text='times up!', font=('Pea Sugar Noodles', 20))
    
    
    
    




    
    
