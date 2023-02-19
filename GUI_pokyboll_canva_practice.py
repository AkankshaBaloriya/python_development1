from tkinter import *

window=Tk()

canva= Canvas(window,width=500,height=500)
canva.create_arc(0,0,500,500,fill="red",extent=180,width=2)
canva.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=2)
canva.create_oval(190,190,310,310,fill="white",width=2)
canva.pack()

window.mainloop()