from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
robot1 = canvas.create_rectangle(500, 500, 480, 480,fill='black')
robot2 = canvas.create_rectangle(100, 100, 105, 105,fill='black')
robot3 = canvas.create_rectangle(95, 90, 105, 110)

def moverobot3(event):
    canvas.move(robot3, 5, 0)
    canvas.move(robot2, 5, 0)
canvas.bind_all('<KeyPress-Return>', moverobot3)
