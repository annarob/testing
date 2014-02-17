from tkinter import *
import random
import time
import sys
tk = Tk()
canvas = Canvas(tk, height=400, width=1800)
canvas.pack()
tk.title('Run')
x1 = 0
x2 = 0
t1= time.time()
robot4 = canvas.create_rectangle(100, 110, 100, 120)
robot2 = canvas.create_rectangle(100, 100, 105, 105,fill='black')
robot3 = canvas.create_rectangle(95, 90, 105, 110)
canvas.move(robot4, 0, 280)
canvas.move(robot2, 0, 280)
canvas.move(robot3, 0, 280)
def run(event):
    canvas.move(robot4, 5, 0)
    canvas.move(robot2, 5, 0)
    canvas.move(robot3, 5, 0)
canvas.bind_all('<KeyPress-1>', run)
def tp(event):
    time.sleep(1.05)
    canvas.move(robot4, 100, 0)
    canvas.move(robot2, 100, 0)
    canvas.move(robot3, 100, 0)
canvas.bind_all('<KeyPress-2>', tp)
def trbo(event):
    time.sleep(0.5)
    for x in range(1, 8):
        tk.update()
        canvas.move(robot4, 25, 0)
        canvas.move(robot2, 25, 0)
        canvas.move(robot3, 25, 0)
        time.sleep(0.05)
canvas.bind_all('<KeyPress-3>', trbo)
def fly(event):
    canvas.move(robot4, 0, -20)
    canvas.move(robot2, 0, -20)
    canvas.move(robot3, 0, -20)
canvas.bind_all('<KeyPress-4>', fly)
def lnd(event):
    canvas.move(robot4, 0, 20)
    canvas.move(robot2, 0, 20)
    canvas.move(robot3, 0, 20)
canvas.bind_all('<KeyPress-5>', lnd)
def sprnt(event):
    canvas.move(robot4, 10, 0)
    canvas.move(robot2, 10, 0)
    canvas.move(robot3, 10, 0)
canvas.bind_all('<KeyPress-6>', sprnt)
def sprtrbo(event):
    time.sleep(2)
    for x in range(1,20):
        tk.update()
        canvas.move(robot4, 50, 0)
        canvas.move(robot2, 50, 0)
        canvas.move(robot3, 50, 0)
        time.sleep(0.05)
canvas.bind_all('<KeyPress-7>', sprtrbo)
def sbmt(event):
    t2 = time.time()
    print(int(t1-t2))
canvas.bind_all('<KeyPress-Return>', sbmt)

        
