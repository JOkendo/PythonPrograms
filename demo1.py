from tkinter import *
class Demo1:
    def __init__(self):
        window = Tk()
        window.title("Widget Demo")

        frame = Frame(window)
        frame.pack()
        
        label = Label(frame, text = "Var1")
        label.pack()

        self.v1 = IntVar()
        entry = Entry(frame, variable = self.v1)
        entry.pack()

        but = Button(frame, text = "Get var1", command = self.v1)
        but.pack()

        window.mainloop()


        def v1(self):
            print("Variable 1 = " + self.v1.get())
Demo1()