from tkinter import *
from tkinter import ttk

def raise_frame(frame):
    frame.tkraise()

master=Tk()
f1 = Frame(master)
f2 = Frame(master)
f1.grid(row=0, column=0, sticky='news')
f2.grid(row=0, column=0, sticky='news')

Label(f1, text='Hyper-Hyper Tic-Tac-Toe', font=("Arial",30)).pack()
Button(f1, text='Start',width=25, command=lambda:raise_frame(f2)).pack()
Button(f1, text="Settings",width=25,command=None).pack() #command=settings
Button(f1, text="Close",width=25,command=master.destroy).pack()

Label(f2, text="Game").pack()


raise_frame(f1)
master.mainloop()