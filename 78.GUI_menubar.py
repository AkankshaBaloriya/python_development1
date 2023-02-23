# learn to do it from another video as well
from tkinter import *

def open():
    print("you opened file")
    
def save():
    print("you saved file")
    
def exit():
    print("you exit file")
    
window=Tk()

menubar=Menu(window)
window.config(menu=menubar)

fileMenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="open",command=open)
fileMenu.add_command(label="save",command=save)
fileMenu.add_separator()
fileMenu.add_command(label="exit",command=exit)



window.mainloop()
