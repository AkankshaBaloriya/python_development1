from tkinter import *
def new_window():
    New= Toplevel() #Toplevel= this creat a new window on the other window on a click,if we remove the main window, new window automaticlly get closed
#-------------------------------------------------------------------------------------- 
def windtk():
    w=Tk()   #create new window but id we remove main window new window foes not go automatically
    window.destroy() #this destroy the main window as soon as new window is created

window= Tk()
#--------------------------------------------------------------------------------------

button=Button(window,text="new window",command=new_window).pack()
button=Button(window,text="window",command=windtk).pack()

window.mainloop()