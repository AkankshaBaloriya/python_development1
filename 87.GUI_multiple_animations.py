from tkinter import *
from ballgroup import *
import time
window=Tk()

WIDTH=500
HEIGHT=500

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

vollyball=ball(canvas,0,0,100,3,3,"red")
tanisball=ball(canvas,30,30,60,6,6,"yellow")
cricket=ball(canvas,80,80,120,5,5,"green")

while True:
    vollyball.move()
    tanisball.move()
    cricket.move()
    window.update()
    time.sleep(0.04)



window.mainloop()