# entry widget=textbox that accept single line of user input

from tkinter import*
def submit():
    username=entry.get()
    print("hello" +" "+ username)
    
    
def deleat():
    entry.delete(0,END)
    
def back():
    entry.delete(len(entry.get())-1,END)
    
window= Tk()

entry=Entry(window,
            font=("arial",50),
            bg="black",
            fg="green"
            )
entry.pack(side=LEFT)

button=Button(window,
              text="submit",
              command=submit)
button.pack(side=RIGHT)

deleat =Button(window,
               text="deleat",
               command=deleat)
deleat.pack(side=RIGHT)

backspace=Button(window,
                 text="backspace",
                 command=back)
backspace.pack(side=RIGHT)

window.mainloop()