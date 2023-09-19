import tkinter as tk
from tkinter import font
'''
class TicTacToeBoard(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Insert Name")
        self._cells = {}

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(master=display_frame,text="Ready?",font=font.Font(size=28,weight="bold"))
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
'''
'''
def init_board(frame:tk.Frame):
    for row in range(3):
        frame.rowconfigure(row, weight=1, minsize=50)
        frame.columnconfigure(row, weight=1, minsize=75)
        for col in range(3):
                button = tk.Button(
                    master=frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                frame.grid._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
'''