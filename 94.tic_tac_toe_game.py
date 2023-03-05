from tkinter import *
import random

def next_turn(row, column):
    global player
    
    if button[row][column]['text']==""and check_winner()is False:
        
        if player==players[0]:
            
            button[row][column]['text']=player
            
            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1]+"turn"))
            elif check_winner()is True:
                label.config(text=(players[0]+"wins"))
                
            elif check_winner=="tie":
                label.config(text="tie!")
                
            else:
                button[row][column]['text']=player
            
            if check_winner() is False:
                player=players[0]
                label.config(text=(players[0]+"turn"))
            elif check_winner()is True:
                label.config(text=(players[1]+"wins"))
                
            elif check_winner=="tie":
                label.config(text="tie!")
                
def check_winner():
    for row in range(3):
        if button[row[0]['text']==button[row[1]['text']]==button[row[2]['text']!="":]]:
            return True
                  

def empty_spaces():
    pass

def new_game():
    pass

window= Tk()
window.title("tic tac toe")
players=["x","o"]
player=random.choice(players)
button=[[0,0,0],[0,0,0],[0,0,0]]
label=Label(text=player +" "+"turn",font=('consolas',40))
label.pack(side="top")

reset_button=Button(text="restart",font=("consolas",20),command=new_game)
reset_button.pack(side="top")

frame=Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        button[row][column]=Button(frame,text="",font=("consolas",40),width=5,height=2,command=lambda row=row,column=column:next_turn(row,column))
        button[row][column].grid(row=row,column=column)
window.mainloop()
