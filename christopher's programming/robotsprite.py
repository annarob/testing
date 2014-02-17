from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_rectangle(100, 100, 105, 105)
canvas.create_rectangle(95, 90, 105, 110)
canvas.create_rectangle(100, 110, 100, 120)

