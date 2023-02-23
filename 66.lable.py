# lable= an area widget to holdtext and/or an image within a window
from tkinter import*
cindow = Tk()
photo=PhotoImage(file='logo.png')
label=Label(cindow,text="Hello akki",
            font=("arial",40,'bold'),
            fg="green",
            bg="black",
            relief=SUNKEN,
            bd=16,
            padx=20,
            pady=20,
            image=photo,
            compound='bottom')
# label.place(x=10,y=0) #to place the text on a particular place on window
label.pack()  #this pack the window according to text or other


cindow.mainloop()

