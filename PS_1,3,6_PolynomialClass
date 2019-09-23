class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    #Returns de coefficient of the x^i term of the polynomial
    def coeff(self, i):
        return self.coefficients[-(i+1)]

    def add(self, other):
        lenSelf = len(self.coefficients)
        lenOther = len(other.coefficients)
        if lenSelf < lenOther:
            minLen = lenSelf
            result = other.coefficients[:]
        else:
            minLen = lenOther
            result = self.coefficients[:]
        for i in range(minLen):
            sumCoeff = self.coeff(i) + other.coeff(i)
            result[-(i+1)] = sumCoeff
        return Polynomial(result)
    
    def mul(self, other):
        lenSelf = len(self.coefficients)
        lenOther = len(other.coefficients)
        lenResult = lenSelf + lenOther - 1 # After multiplying coeffs with the highest degree, resulting list has length of lenResult
        result = [0] * lenResult # Create list of zeros
        for i in range(lenSelf):
            for j in range(lenOther):
                result[-(i+j+1)] += self.coeff(i) * other.coeff(j)
        return Polynomial(result)

    def __str__(self):
        result = ''
        i = len(self.coefficients)-1
        for coeff in self.coefficients:
            if i > 1:
                result += str(coeff) + 'z**' + str(i) + ' + '
            elif i == 1:
                result += str(coeff) + 'z' + ' + '
            else:
                result += str(coeff)
            i = i-1
        return result

    def val(self, v):
        selfLen = len(self.coefficients)
        result = 0
        for i in range(selfLen):
            result += self.coeff(i) * (v**i)
        return result

    def roots(self):
        lenSelf = len(self.coefficients)
        if lenSelf == 3:
            a = self.coeff(2)
            b = self.coeff(1)
            c = self.coeff(0)
            if a == 0:
                return [-c/b]
            else:
                determinant = b**2 - 4*a*c
                res1 = (-b - complex(determinant)**0.5)/(2*a)
                res2 = (-b + complex(determinant)**0.5)/(2*a)
                if determinant < 0:
                    return [res1, res2]
                else:
                    return [res1.real, res2.real]
        elif lenSelf == 2:
            b = self.coeff(1)
            c = self.coeff(0)
            return [-c/b]
        elif lenSelf == 1:
            c = self.coeff(0)
            result = complex(c)**0.5 if c<0 else c**0.5
            return [result]
        else:
            return "Order too high to solve for roots."
            

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __call__(self, x):
        return self.val(x)

    def __repr__(self):
        return str(self)

p1 = Polynomial([1, 2, 3])
print p1
p2 = Polynomial([100, 200])
print p1.add(p2)
print p1 + p2
print p1(1)
print p1(-1)
print (p1 + p2)(10)
print p1.mul(p1)
print p1 * p1
print p1 * p2 + p1
print p1.roots()
print p2.roots()
p3 = Polynomial([3, 2, -1])
print p3.roots()
print (p1 * p2).roots()
                    
            
