from tkinter import *
import random
tk = Tk()
def respond():
    response = ['Rock', 'Paper', 'Scissors']
    print(random.choice(response))
btn = Button(tk, text="Go", command=respond)
btn.pack()
