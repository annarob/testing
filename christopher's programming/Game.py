from tkinter import *
tk = Tk()
tk.title('Game Menu')
def begingame():
    canvas = Canvas(tk, width=500, height=500)
    canvas.pack()
    tk.title('Squirrel Nut Quest')
    pass
btn = Button(tk, text="New Game", command=begingame)
btn.pack()


