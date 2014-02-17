from tkinter import *
tk = Tk()
canvas = Canvas(tk, height=500, width=500)
canvas.pack()
fn1 = canvas.create_polygon(80, 80, 85, 85, 80, 90, 95, 85, fill='#ffd800')
