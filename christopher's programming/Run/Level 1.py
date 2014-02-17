from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, height=400, width=1800)
canvas.pack()
tk.title('Run')
x1 = 0
x2 = 0
t1 = time.time()
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
def sbmt(event):
    t2 = time.time()
    print(int(t1-t2))
canvas.bind_all('<KeyPress-Return>', sbmt) 
          
    
    

    
    
