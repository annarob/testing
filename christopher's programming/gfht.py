from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
fn2 = canvas.create_polygon(70, 80, 85, 85, 120, 85, fill='cyan')
