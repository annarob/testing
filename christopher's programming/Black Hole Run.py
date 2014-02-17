from tkinter import *
import time
import random
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
fn1 = canvas.create_polygon(80, 80, 85, 85, 80, 90, 95, 85, fill='#ffd800')
bhl = canvas.create_oval(0, 0, 50, 500, fill='black')
tk.title('Black Hole Run')
def movefn1(event):
    canvas.move(fn1, 3, 0)
canvas.bind_all('<KeyPress-Return>', movefn1)
for x in range(1, 500):
    canvas.move(fn1, -2, 0, )
    time.sleep(0.05)
    tk.update()
print('Level 1 complete!')
time.sleep(5)
for x in range(1, 600):
    canvas.move(fn1, -3, 0, )
    time.sleep(0.05)
    tk.update()
print('Level 2 complete!')
print('Turbo Unlocked! Press tab to activate.')
def turbo(event):
    time.sleep(1)
    for x in range(1, 10):
        canvas.move(fn1, 12, 0)
        time.sleep(0.05)
        tk.update()
canvas.bind_all('<KeyPress-Tab>', turbo)
print('BOSS LEVEL: Vlad the Inhaler')
time.sleep(5)
for x in range(1, 600):
    canvas.move(fn1, -5, 0, )
    time.sleep(0.05)
    tk.update()
print('Vlad the Inhaler defeated')
time.sleep(5)
for x in range(1, 600):
    canvas.move(fn1, -3, 0, )
    time.sleep(0.03)
    tk.update()
print('level 4 complete!')
time.sleep(5)
for x in range(1, 600):
    canvas.move(fn1, -5, 0, )
    time.sleep(0.06)
    tk.update()
print('level 5 complete')
print('warp unlocked! press 1 to activate')
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
print('Suction cup defeated')
print('UPGRADE!!!!')
fn2 = canvas.create_polygon(70, 80, 85, 85, 120, 85, fill='cyan')
canvas.move(fn1, 0, 9999)
def mvefn2(event):
    canvas.move(fn2, 10, 0)
canvas.bind_all('<KeyPress-Return>', mvefn2)
time.sleep(5)
for x in range(1, 650):
    canvas.move(fn2, -6, 0, )
    time.sleep(0.05)
    tk.update()
print('level 7 complete!')
print('HyperJump unlocked! press tab to activate')
def hjmp(event):
    canvas.move(fn2, (random.randrange(100)), 0)
canvas.bind_all('<KeyPress-Tab>', hjmp)




      







