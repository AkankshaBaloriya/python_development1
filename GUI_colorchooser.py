# GUI colorchooser
def click():
    color=colorchooser.askcolor()
    a=color[1]
    # print(a)
    window.config(bg=a)
from tkinter import *
from tkinter import colorchooser    #submodule
window = Tk()
window.geometry("420x420")
button=Button(window,
              text="choose",
              command=click,)
button.pack()

window.mainloop()