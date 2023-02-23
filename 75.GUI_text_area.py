# text area
# text widget= allow to write multiple lines of text and provide text area for that
def submit():
    a= text.get("1.0",END)
    print(a)
from tkinter import*

window= Tk()

text=Text(window,
          bg="light blue",
          font=("Ink Free",25),
          width=20,
          height=8,
          padx=10,
          pady=10)
text.pack()
btn= Button(window,
            text="submit",
            command=submit)
btn.pack()
window.mainloop()

