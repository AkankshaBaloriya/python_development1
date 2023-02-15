# button =you click it, then it does stuff

from tkinter import *
count=0

def click():
    global count
    count+=1
    print(f"i am clicked {count} times ")


window=Tk()

image=PhotoImage(file="logo.png")

button =Button(window,
               text='click here',
               command=click,
               font=("Comic Sans",30),
               fg="green",
               bg="black",
               activeforeground="yellow",
               activebackground="pink",
            #    state=DISABLED
            image=image,
            compound=TOP)

button.pack()
window.mainloop()

