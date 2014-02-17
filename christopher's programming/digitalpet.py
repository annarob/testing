from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=150, height=130)
canvas.pack()
import time
tk.title('Digital Pet')
c = colorchooser.askcolor()
pet = canvas.create_oval(10, 10, 25, 25, fill=c[1])
for x in range(1, 100):
    canvas.move(pet, 0, 1)
    tk.update()
    time.sleep(0.01)
    pass
for x in range(1, 5):
    time.sleep(3)
    for x in range(1, 80):
        canvas.move(pet, 1, 0)
        tk.update()
        time.sleep(0.05)
    time.sleep(2)
    for x in range(1, 80):
        canvas.move(pet, -1, 0)
        tk.update()
        time.sleep(0.05)
    poop = canvas.create_oval(10, 110, 25, 130, fill='brown')
def feedpet(event):
    time.sleep(50)
canvas.bind_all('<KeyPress-1>', feedpet)
canvas.move(pet, 15, 0)
canvas.itemconfig(pet, fill='red')
print('you lose')
tk.title('Game Over')

    



    


