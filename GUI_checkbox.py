# checkbutton widget =checkbox can check only one out of all
from tkinter import *

def display():
    if (x.get()==1):
        print("you agree")
    else:
        print("not agree")
        
window=Tk()

x=IntVar()

checkbox =Checkbutton(window,
                      text="i agree to this",
                      variable=x,
                      onvalue=1,
                      offvalue=0,
                      command=display,
                      font=('arial',20),
                      fg="green",
                      bg="gray",
                      activeforeground="green",
                      activebackground="gray",
                      padx=25,
                      pady=10)
checkbox.pack()

window.mainloop()