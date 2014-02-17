from tkinter import *
tk = Tk()
def hello():
    print('hello there')
btn = Button(tk, text="click me", command=hello)
btn.pack()

