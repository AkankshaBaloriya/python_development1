from tkinter import *
def upward(evenrdt):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
    
def downward(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
    
def forward(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())
    
def backward(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
#------------------------------------------------------------------------------------------

def up(evenrdt):
    label1.place(x=label1.winfo_x(),y=label1.winfo_y()-10)
    
def down(event):
    label1.place(x=label1.winfo_x(),y=label1.winfo_y()+10)
    
def ahead(event):
    label1.place(x=label1.winfo_x()+10,y=label1.winfo_y())
    
def back(event):
    label1.place(x=label1.winfo_x()-10,y=label1.winfo_y())
    
    
     
window=Tk()
window.geometry("600x600")
image=PhotoImage(file="car.png")
image=image.subsample(-7,7)
image1=PhotoImage(file="car.png")
image1=image.subsample(-7,7)

window.bind("<w>",upward)
window.bind("<d>",forward)
window.bind("<a>",backward)
window.bind("<s>",downward)

window.bind("<Up>",up)
window.bind("<Down>",ahead)
window.bind("<Left>",back)
window.bind("<Right>",down)

label=Label(window,image=image)
label.place(x=1,y=2)

label1=Label(window,image=image)
label1.place(x=1,y=100)

window.mainloop()