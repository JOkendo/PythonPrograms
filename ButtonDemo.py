from tkinter import *

class ButtonDemo:
    def __init__(self):
        window = Tk()
        butOk = Button(window, text ="OK", bg = "black", command = self.processOk)
        butC = Button(window, text = "CANCEl", bg = "yellow", command = self.processC)
        butOk.pack()
        butC.pack()

        window.mainloop()

    def processOk(self):
        print("Ok")

    def processC(self):
        print("Cancel")

ButtonDemo()
