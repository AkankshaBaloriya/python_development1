from tkinter import *
from time import *

def update():
    tstring=strftime("%I:%M:%S %P")
    tlabel.config(text=tstring)
    
    dsrting=strftime("%A")
    dlabel.config(text=dsrting)
    
    datestring=strftime("%B %D, %Y")
    datelabel.config(text=datestring)
window=Tk()

tlabel=Label(window,bg="black",fg="green",font=("Arial",100))
tlabel.pack()

dlabel=Label(window,font=("Arial",100))
dlabel.pack()

datelabel=Label(window,font=("Arial",100))
datelabel.pack()

update()
window.mainloop()