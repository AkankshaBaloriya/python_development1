# GUI scale

from tkinter import *

def submit():
    print("the temp. is " +str(scale.get()) + " " + "degree")
window=Tk()

# image= PhotoImage(file='logo.png')
# label=Label(image=image)               #used to give lable image
# label.pack()
scale =Scale(window, #scale create the scale (like tharmameter scale and all)
             from_=100,
             to=0, #specify scale volume
             length=400,  #increse size of scale
             orient=VERTICAL,  # changes angle of the scale
             showvalue=0, #hide current value
             tickinterval=10,
             troughcolor='red',
             fg='black',
             bg='yellow',
             ) #adds numeric indicater for value
scale.set(50)
scale.pack()

button=Button(window,
              command=submit,
              text="submit")
button.pack()

window.mainloop()