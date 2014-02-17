from tkinter import*
import time
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
def ovals(width, height):
    for x in range(0, 30):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = random.randrange(x1 + random.randrange(width))
        y2 = random.randrange(y1 + random.randrange(height))
        canvas.create_oval(x1, y1, x2, y2, outline='#33ff33', fill='#009900')
        pass
    for x in range(0, 100):
        canvas.move(random.randrange(3), random.randrange(3), random.randrange(3))
        canvas.update()
        time.sleep(0.05)
        pass
    
