from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
fn1 = canvas.create_polygon(80, 80, 85, 85, 80, 90, 95, 85, fill='#ffd800')
print('UPGRADE!!!!')
fn2 = canvas.create_polygon(70, 80, 85, 85, 120, 85, fill='cyan')
canvas.move(fn1, 0, 9999)
def mvefn2(event):
    canvas.move(fn2, 10, 0)
canvas.bind_all('<KeyPress-Return>', mvefn2)
time.sleep(5)
for x in range(1, 650):
    canvas.move(fn2, -5, 0, )
    time.sleep(0.05)
    tk.update()
print('level 7 complete!')
