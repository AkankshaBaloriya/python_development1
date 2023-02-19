from tkinter import *

window= Tk()

canva=Canvas(window,width=500,height=500)
canva.create_line(0,0,500,500,fill="red",width=2)
canva.create_line(0,500,500,0,fill="blue",width=2)
canva.create_rectangle(70,70,100,100,fill="light yellow",width=1)
point=[50,0,50,50,0,50]
canva.create_polygon(point,fill="red",width=1)
canva.create_arc(0,380,300,50,fill="light green",style=CHORD,start=180)

canva.pack()

window.mainloop()