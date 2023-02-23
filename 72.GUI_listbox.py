# listbox = allow us to select items

def submit():
    food=[]
    print("your orderd" +" "+ list.get(list.curselection()))

def add():
    list.insert(list.size(),entry.get())
    list.config(height=list.size())
    
def remove():
    list.delete(list.curselection())
    list.config(height=list.size())
from tkinter import*

window=Tk()

list=Listbox(window,
             bg="#f7ffde",
             font=("constantia",20),
             width=10)
            #  selectmode=MULTIPLE
list.pack()
list.insert(1,"pizza")
list.insert(2,"pasta")
list.insert(3,"noodles")
list.insert(4,"garlic bread")
list.insert(5,"samosa")

list.config(height=list.size())
entry=Entry(window)
entry.pack()

button=Button(window,
              text="order",
              command=submit)
button.pack(side=LEFT)

button=Button(window,
              text="add",
              command=add)
button.pack(side=RIGHT)

button=Button(window,
              text="remove",
              command=remove)
button.pack()

window.mainloop()