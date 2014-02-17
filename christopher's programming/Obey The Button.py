from tkinter import *
import random
import time
tk = Tk()
easy1 =('that was easy.')
canvas = Canvas(tk, height=50, width=50)
global btn
def respond():
    time.sleep(0.5)
    response = ['DO NOT press the button.', 'I said DON\'T.','*AHEM*','I\'d like to see you press it again.',
                'on the count of three, STOP. 1... 2... 3!','Just don\'t press the button.',
                '*BOOM!*', 'Press the button one more time, and I will spank you.','smart alek.', 'FINE, just one more time.',
                'AHHH! BEHIND YOU!', 'I don\'t care. Press it again.NOT!', 'Get off the computer, you\'ve been on forever!',
                'Have pity on me and do not press it again.', 'Go check out the weather', 'SSSSSSSSTTTTTTTOOOOOOPPPPPPP!!!!!!!!',
                'You think you are so smart.','Go read a book.', 'Look, i\'ts 3:00 already!',
                'Oh look. A flaming blimp packed with explosives.','I will give you candy.']
    print(random.choice(response))
btn = Button(tk, text="DO NOT PRESS", command=respond)
btn.pack()
