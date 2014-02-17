from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
scsprite = canvas.create_oval(480, 480, 500, 500, fill='blue')
