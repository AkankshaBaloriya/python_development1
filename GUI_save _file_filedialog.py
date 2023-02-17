from tkinter import *
from tkinter import filedialog

def save():
    file=filedialog.asksaveasfile()
    filetext=str(text.get("1.0",END))
    file.write(filetext)
    file.close()
window=Tk()

button=Button(window,
              command=save,
              text="save")
button.pack()
text=Text(window)
text.pack()

window.mainloop()
