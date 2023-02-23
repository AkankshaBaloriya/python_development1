from tkinter import *
from tkinter import ttk

window=Tk()

notebook=ttk.Notebook(window) #widget that manages a colection oof windows/displays
tab1=Frame(notebook) #new frame for tab1
tab2=Frame(notebook) #new frame for tab2

notebook.add(tab1,text="tab 1")
notebook.add(tab2,text="tab 2")
notebook.pack(expand=TRUE, fill="both") #USED TO EXPAND THE GAP NOT OTHERWISE
                                        #fill = fill space on x and y axis

Label(tab1,text="this is tab 1",width=50,height=25).pack()
Label(tab2,text="this is tab 2",width=50,height=25).pack()


window.mainloop()