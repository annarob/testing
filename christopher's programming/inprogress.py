from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
import time
plyr1f = canvas.create_arc(250, 500, 270, 480, extent=359, style=ARC, fill='#ffd800')
obl = canvas.create_rectangle(0, 0, 150, 150, fill='black')
obl2 = canvas.create_rectangle(0, 0, 150, 150, fill='black')
canvas.move(obl2, 500, 150)
def moveright(event):
    canvas.move(plyr1f, 5, 0)
canvas.bind_all('<KeyPress-Right>', moveright)
def moveleft(event):
    canvas.move(plyr1f, -5, 0)
canvas.bind_all('<KeyPress-Left>', moveleft)
def fire(event):
    for x in range(1, 50):
        for x in range(1, 50):
            canvas.move(plyr1f, 0, -10)
            time.sleep(0.05)
            tk.update()
        canvas.move(plyr1f, 0, 490)
canvas.bind_all('<KeyPress-Return>', fire)
for x in range(1, 50):
    for x in range(1, 50):
        canvas.move(obl, 10, 0)
        canvas.move(obl2, 10, 0)
        time.sleep(0.05)
        tk.update()
    for x in range(1, 50):
        canvas.move(obl, -10, 0)
        canvas.move(obl2, -10, 0)
        time.sleep(0.05)
        tk.update()
    
    
    
                


    
    
    


