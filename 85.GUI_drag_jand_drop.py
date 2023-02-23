from tkinter import *
def drag(event):
    label.a=event.x
    label.b=event.y

def motion(event):
    x=label.winfo_x() - label.a + event.x
    y=label.winfo_y() - label.b + event.y
    label.place(x=x,y=y)
    
window=Tk()

label=Label(window,
            bg="red",
            width=8,
            height=4)
label.place(x=1,y=1)
label.bind("<Button-1>",drag)
label.bind("<B1-Motion>",motion)



window.mainloop()