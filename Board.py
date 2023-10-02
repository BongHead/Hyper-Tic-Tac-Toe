from tkinter import *
from tkinter.ttk import *
from tkinter import font
from enum import Enum
import numpy as np

class TileStates(Enum):
    BLANK = 0
    X = 1
    O = 2
    WON = 3

class Board(Tk):
    def __init__(self) -> None:
        super.__init__()
        self.title("Title")

    def getWin()->tuple:#self?
        return ([0,1,2],
                [3,4,5],
                [6,7,8],
                [0,3,6],
                [1,4,7],
                [2,5,8],
                [0,4,8],
                [2,4,6]) #winCons = Board.getWin()
    
    def checkRows(board:list):
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return 0
    
    def checkDiagonals(board:list): 
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0
    
    def checkWin(board:list):
    #transposition to check rows, then columns
        for newBoard in [board, np.transpose(board)]:
            result = Board.checkRows(newBoard)
            if result:
                return result
        return Board.checkDiagonals(board)
    
    def init_board(frame:Frame):
        pass

        
class NestedBoard(Board):
    def __init__(self) -> None:
        pass
      

class NestedNestedBoard(NestedBoard):
    def __init__(self) -> None:
        pass
    
