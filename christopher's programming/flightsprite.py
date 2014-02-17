from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=1000, height=800)
canvas.pack()
canvas.create_rectangle(100, 100, 105, 105)
canvas.create_rectangle(95, 90, 105, 110)
canvas.create_line(102, 90, 102, 80)
canvas.create_line(107, 75, 97,  80)
canvas.create_line(107, 80, 97, 75)
