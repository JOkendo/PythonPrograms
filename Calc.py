'''Class Calculator'''

class Calc:
    def __init__(self, v1, v2):
        self.__v1 = v1
        self.__v2 = v2


    def getV1(self):
        return self.__v1
    
    def getV2(self):
        return self.__v2

    def setV1(self, v1):
        self.__v1 = v1

    def setV2(self, v2):
        self.__v2 = v2

    def add(self):
        result = self.getV1() + self.getV2()
        print("Sum = ", result)
        return result

    def sub(self):
        if self.getV2() < self.getV1():
            result = self.getV1() - self.getV2()
            print("Difference = ", result)
            return result
        else:
            result1 = self.getV2() - self.getV1()
            print("Difference = ", result1)
            return result1

    def mul(self):
        result = self.getV1() * self.getV2()
        print("Product = ", result)
        return result
    
    def divi(self):
        if self.getV2() > 0:
            result = self.getV1() / self.getV2()
            print("Division = ", result)
            return result

    def mod(self):
        result = self.getV1() % self.getV2()
        print("Remainder = ", result)
        return result

def main():
    calc = Calc(2, 3)
    calc.add()
    calc.sub()
    calc.mul()
    calc.divi()
    calc.mod()
    

main()