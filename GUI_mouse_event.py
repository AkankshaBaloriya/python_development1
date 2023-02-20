from tkinter import *
def up(event):
    print("upside")
    
def down(event):
    print("downside" +str(event.x)+","+str(event.y))  #str(event.x)=this shows the location in number where we clicked on
    
def middle(event):
    print("middle")
    
def release(event):
    print("released")
    
def enter(event):
    print("entered")
    
def leave(event):
    print("leave")
  
def motion(event):
    print("here"+str(event.x)+","+str(event.y))
      
window= Tk()

window.bind("<Button-1>",up)
window.bind("<Button-3>",down)
window.bind("<Button-2>",middle)
window.bind("<ButtonRelease>",release)
window.bind("<Enter>",enter)
window.bind("<Leave>",leave)
window.bind("<Motion>",motion)

window.mainloop()