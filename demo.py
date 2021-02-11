from tkinter import *

def okBut():
    print("Ok Button pressed!")
def canBut():
    print("Cancel Button pressed!")

window = Tk()
window.title("Jack Okendo")
label = Label(window, text = "GUI Demo")
butOk = Button(window, text = "OK", fg = "black", bg = "green", command = okBut)
butCanc = Button(window, text = "CANCEL", fg = "white", bg = "red", command = canBut)
label.pack()
butOk.pack()
butCanc.pack()
window.mainloop()