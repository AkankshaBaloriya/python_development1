from tkinter import*
def doit(event):
    window.destroy()
    print("you quit")
    
def write(event):
    print("you are writing")
    
# def any(event):
    # print("you doing anything with "+ event.keysym)
    # label.config(text=event.keysym)
    
window= Tk()

window.bind("<q>",doit)
window.bind("<w>",write)
# window.bind("<key>",any)

label=Label(window)
window.mainloop()