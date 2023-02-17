# filedialog= for open the file,writing or reading and all

from tkinter  import *
from tkinter import filedialog

def open():
    filepath=filedialog.askopenfilename(initialdir="",
                                        title='open',
                                        filetypes=(('txt',"text"),('all files','*.*')))
    file=open(filepath)
    print(file.read())
    file.close()
window= Tk()

button=Button(window,
              text="open",
              command=open)
button.pack()

window.mainloop()