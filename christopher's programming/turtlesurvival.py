print('welcome to turtle survival.')
print('type start() to begin.')
print('type health to see your health.')
def start():
    wn = turtle.Screen()
    t = turtle.turtle()
    t.up()
    pass
def forward(size):
    t.forward(size)
    pass
def back(size):
    t.backward(size)
    pass
def up(size):
    t.left(90)
    t.forward(size)
    t.right(90)
    pass
def down(size):
    t.right(90)
    t.forward(size)
    t.left(90)
    pass
health = (5)
tht = (1)
def hurt():
    health - tht
    if health == 0:
        t.reset()
        pass
    pass
