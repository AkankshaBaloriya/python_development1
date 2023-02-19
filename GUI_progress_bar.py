# need to understand one more time i guess
from tkinter import *
from tkinter.ttk import *
import time
def start():
    task=10
    x=0
    while(x<task):
        time.sleep(1)
        bar['value']+=10
        x+=1
        window.update()
        percent.set(str(int((x/task)*100))+"%")
        text.set(str(x)+"/"+str(task)+"task completed")

window=Tk()
percent=StringVar()
text=StringVar()

bar=Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=40)

percentLable=Label(window,textvariable=percent).pack()
taskLable=Label(window,textvariable=text).pack()
button=Button(window,text="download",command=start).pack()

window.mainloop()