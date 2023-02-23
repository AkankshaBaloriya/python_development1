# radiobutton =similar to checkbox but in this we can select only one
from tkinter import *

a=["pizza","burger","pasta"]

def order():
    if (x.get()== 0):
        print("you orderd pizza")
    elif (x.get()== 1):
        print("you orderd burger")
    elif (x.get()== 0):
        print("you orderd pasta")
    else:
        print("no order")

window=Tk()

image=PhotoImage(file="logo.png")
imagee=PhotoImage(file="logo.png")
imageo=PhotoImage(file="logo.png")

b=[image,imagee,imageo]

x=IntVar()

for i in range(len(a)):
    radio=Radiobutton(window,
                      text=a[i],  #adds text to radui button
                      variable=x,  #groups radio button togesther if they share same variable
                      value=i, #this assign a different value to each radiobutton
                      font=("airel",50),
                      padx=25,
                      image=b[i],
                      compound=LEFT,
                    #   indicator=0,
                      height=200,
                      command=order)
    radio.pack()

window.mainloop()