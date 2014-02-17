
import time
class pyhelp:
    def convert(self, value):
        print('%x' % value)
    def amath(self, addend1, addend2):
        add = (addend1 + addend2)
        print('%s' % (str(add)))
    def smath(self, addend1, addend2):
        add = (addend1 - addend2)
        print('%s' % (str(add)))
    def dmath(self, addend1, addend2):
        add = (addend1 / addend2)
        print('%s' % (str(add)))
    def mmath(self, addend1, addend2):
        add = (addend1 * addend2)
        print('%s' % (str(add)))
    def about(self):
        print('pyhelp is a python tool to help create programs')
        print('it is a work in progress')
        print('it is created by cbroc inc.')
    def decimal(self, numerator, denominator):
        dec = (numerator / denominator)
        print('%s' % (str(dec)))
    def convtempf(self, farenheit):
        f = farenheit
        c = (f - 32) * (100 / 180)
        c2 = (str(c))
        print(c2)
    def convtempc(self, celsius):
        c = celsius
        f =  (c * (180 / 100)) + 32
        f2 = (str(f))
        print(f2)
    def square(self, value):
        v = value
        squareroute = v * value
        print('%s' % (str(squareroute)))
    def cube(self, value):
        v = value
        v2 = value
        squareroute = (v * value) * v2
        print('%s' % (str(squareroute)))
pyhelp = pyhelp()

    
        
    
      



      
