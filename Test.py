#This is because I am too lazy to make a testing branch. Later on just copy-paste everything in main.py
from tkinter import *
from tkinter import ttk
from Board import *
from tkinter import font
#from game import *  (Get all the game logic)

def raise_frame(frame):
    frame.tkraise()

master=Tk()
master.title("Hyper Hyper Tic-Tac-Toe")
master.geometry() #change size of window
master.resizable(0,0)
f1 = Frame(master)
f2 = Frame(master)
f1.grid(row=0, column=0, sticky='news')
f2.grid(row=0, column=0, sticky='news')

Label(f1, text='Hyper Hyper Tic-Tac-Toe', font=("Arial",30)).pack()
Button(f1, text='Start',width=25, command=lambda:raise_frame(f2)).pack()
Button(f1, text="Settings",width=25,command=None).pack() #command=settings
Button(f1, text="Close",width=25,command=master.destroy).pack()

Label(f2, text="Game",font=("Arial", 30)).pack() #config text to change turn i.e "X to play/O to play"
for row in range(3):
    for col in range(3):
        Button(f2,height=4,width=8).pack()

raise_frame(f1)
master.mainloop()