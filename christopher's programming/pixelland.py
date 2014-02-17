print('welcome to pixelland. copyright cbroc inc.')
print('type credits for game credits')
print
class player:
    def forward(self):
        print('moved forward 1 step')
    def right(self):
        print('moved right 1 step')
    def left(self):
        print('moved left 1 step')
    def backward(self):
        print('moved backward 1 step')
    pass
sam = player()
forward = sam.forward()
backward = sam.backward()
right = sam.right()
left = sam.left()
        
    


