# messagebox 
def click():
    # messagebox.showinfo(title="info",message="you are a animal")   #showinfo
    # messagebox.showwarning(title="warn",message="we are giving you warning")    #showwarning
    # messagebox.showerror(title="error",message="there is virus ")    #showerror
    # messagebox.askyesno(title="choose",message="are you human")    #askyesno
    # messagebox.askyesnocancel(title="choose",message="continue downloading")  #askyesnocancel
    # if messagebox.askokcancel(title="q.",message="you wanna play"):
    #     print("you did it")
    # else:
    #     print("you dont want to")                           #askokcancel
    messagebox.askretrycancel(title="what to do",message="retry or cancel",icon='error')    #askretrycancel,  #icon to set different log
    
from tkinter import*
from tkinter import messagebox  #import messagebox liabrary
window=Tk()

button=Button(window,
              command=click,
              text="click")
button.pack()

window.mainloop()