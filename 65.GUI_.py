#GUI =grafical user interface
# widges =GUI element :button,texterea,lables,images
# windows= serves as a container to hold or contain these widgetsn 

from tkinter import*

window=Tk()  #instanciate a instance of a window
window.geometry("420x420")  #geometry to change the size of window
window.title("Akki")  #title is for changing title of the window
window.config(background="gray") #changes the background color
icon=PhotoImage(file="logo.png") #this is to change logo on window if there is one
window.iconphoto(True,icon)


window.mainloop()       #this will place window on  computer screen. listen for events