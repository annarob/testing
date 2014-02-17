from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
fn1 = canvas.create_polygon(80, 80, 85, 85, 80, 90, 95, 85, fill='#ffd800')
bhl = canvas.create_oval(0, 0, 50, 500, fill='black')
tk.title('Black Hole Run')
def movefn1(event):
    canvas.move(fn1, 3, 0)
canvas.bind_all('<KeyPress-Return>', movefn1)
def turbo(event):
    time.sleep(1)
    for x in range(1, 10):
        canvas.move(fn1, 12, 0)
        time.sleep(0.05)
        tk.update()
canvas.bind_all('<KeyPress-Tab>', turbo)
def warp(event):
    time.sleep(1)
    canvas.move(fn1, -30, 0)
    time.sleep(1)
    canvas.move(fn1, 60, 0)
canvas.bind_all('<KeyPress-1>', warp)
print('BOSS LEVEL: Suction Cup')
time.sleep(5)
for x in range(1, 30):
    for x in range(1, 10):
        canvas.move(fn1, -5, 0, )
        time.sleep(0.05)
        tk.update()
    canvas.move(fn1, -15, 0)
print('
