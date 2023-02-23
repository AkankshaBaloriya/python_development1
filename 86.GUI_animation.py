from tkinter import *
import time
WIDTH=500
HEIGHT=500
x=1
y=1

window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT)

canvas.pack()
photo=PhotoImage(file="ufo.png")
imagee=photo.subsample(-8,8)
image=canvas.create_image(0,0,image=imagee,anchor=NW)

image_width=photo.width()
image_height=photo.height()
while True:
    coord=canvas.coords(image)
    print("coor")
    if(coord[0]>=WIDTH-image_width or coord[0]<0):
        x= -x
    # if(coord[1]>HEIGHT-image_height or coord[1]<0):
    #     y= -y
    canvas.move(image,x,0)
    window.update()
    time.sleep(0.01)

window.mainloop()