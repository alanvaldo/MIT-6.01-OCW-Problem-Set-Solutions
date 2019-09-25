class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ('V2[' + str(self.x) + ',' + str(self.y) + ']')

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def add(self, vector):
        xSum = self.x + vector.x
        ySum = self.y + vector.y
        return V2(xSum, ySum)

    def mul(self, a):
        return V2(a*self.x, a*self.y)

    def __add__(self, vector):
        return self.add(vector)

    def __mul__(self, a):
        return self.mul(a)

print '1.',
print V2(1.1,2.2)

print '2.',
v = V2(1.0, 2.0)
print v.getX()
print v.getY()

print '3.',
a = V2(1.0, 2.0)
b = V2(2.2, 3.3)
print a.add(b)
print a.mul(2)
print a.add(b).mul(-1)

print '4.',
print V2(1.1, 2.2) + V2(3.3, 4.4)
print V2(1.0, 2.0) * 2
        

    
