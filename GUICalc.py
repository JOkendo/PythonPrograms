'''GUI Calculator'''
from tkinter import *

class GUICalc:
    def __init__(self, v1, v2):
        window = Tk()
        window.title("GUI Calcutator")

        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()

        entry = Entry(frame1, text = "Enter Number1", variable = self.v1, command = self.setV1 )
        entry.pack()


        window.mainloop()



    def setV1(self, v1):
        self.v1 = v1

    def setV2(self, v2):
        self.v2 = v2

    def add(self):
        result = self.v1 + self.v2
        print("Sum = ", result)
        return result

    def sub(self):
        if self.v2 < self.v1:
            result = self.v1 - self.v2
            print("Difference = ", result)
            return result
        else:
            result1 = self.v2 - self.v1
            print("Difference = ", result1)
            return result1

    def mul(self):
        result = self.v1 * self.v2
        print("Product = ", result)
        return result
    
    def divi(self):
        if self.v2 > 0:
            result = self.v1 / self.v2
            print("Division = ", result)
            return result

    def mod(self):
        result = self.v1 % self.v2
        print("Remainder = ", result)
        return result

def main():
    calc = GUICalc(2, 3)
    calc.add()
    calc.sub()
    calc.mul()
    calc.divi()
    calc.mod()
    

main()