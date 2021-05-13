
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    # create the constructor to show how the data object is created
    def __init__(self, top, bottom) -> None:
        self.num = top
        self.den = bottom

    def __str__(self):
        """convert object into a string"""
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __eq__(self, otherfraction):
        numone = self.num*otherfraction.den
        numtwo = self.den*otherfraction.num

        return numone == numtwo
    
    def __le__(self, otherfraction):
        numone = self.num/self.den
        numtwo = otherfraction.num/otherfraction.den

        return numone <= numtwo
    
    def __lt__(self, otherfraction):
        cond1 = self.__le__(otherfraction)
        cond2 = self.__eq__(otherfraction)
        
        return cond1 & cond2

    def __gt__(self, otherfraction):

        cond1 = self.__lt__(otherfraction)

        return not cond1
    

    def __ge__(self, otherfraction):
        cond1 = self.__gt__(otherfraction)
        cond2 = self.__eq__(otherfraction)

        return cond1 or cond2

    def __mul__(self, otherfraction):
        numone = self.num * otherfraction.num
        numtwo = self.den * otherfraction.den
        common = gcd(numone, numtwo)

        return Fraction(numone//common, numtwo //common)

    def __truediv__(self, otherfraction):
        numone = self.num * otherfraction.den
        numtwo = self.den * otherfraction.num
        common = gcd(numone, numtwo)

        return Fraction(numone//common, numtwo //common)
    
    def __sub__(self,otherfraction):
        newnum = (self.num*otherfraction.den) - (otherfraction.num*self.den)
        newden = (self.den*otherfraction.den)
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)


f1 = Fraction(1,2)
f2 = Fraction(1,4)
f1 <= f2
f1 < f2
f1 > f2
f1 >=f2
f3  = f1 * f2
print(f3)
print(f1 / f2)
print(f1 - f2)
print(f2 - f1)

x = Fraction(1,2)
y = Fraction(2,3)

print(x+y)
print(x == y)



# 1.13.2 Inheritance
class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):

    def __init__(self,n):
        super(AndGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

g1 = AndGate("G1")
>>> g1.getOutput()