import math
SIZE = 9
SUDOKU = 3

def addQueen(board, col): 
    if col >= SIZE:
        #Reached the end of the board, meaning it was successful!
        return True
    
    for row in range(SIZE):
        #For each row, place a queen if safe
        if safeLocation(board, row, col): 
            board[row][col] = True
            if addQueen(board, col + 1):
                #If the next queen is added (==true) return True
                return True
            else: 
                board[row][col] = False
    #If the iteration breaks, there was no possible way
    return False

def safeLocation(board, row, col):
    #Assume it is safe
    result = True
    for r in range(SIZE):
        #Checks row
        if r != row:
            #If there is a True item in the list, means that there is a Q there
            if board[r][col] == True:
                result = False
        #Checks Column
        if r != col:
            if board[row][r] == True:
                result = False
    #Checks safe or not in NW direction
    for nw in range(min(row, col)):
        if board[row - (nw + 1)][col - (nw + 1)] == True:
            result = False
    #Checks SW direction
    for sw in range(min(SIZE - row - 1, col)):
        if board[row + sw + 1][col - (sw + 1)] == True:
            result = False
    #Checks NE direction
    for ne in range(min(row, SIZE - col - 1)):
        if board[row - (ne + 1)][col + ne + 1] == True:
            result = False
    #Check SE direction
    for se in range(min(SIZE - row - 1, SIZE - col - 1)):
        if board[row + se + 1][col + se + 1] == True:
            result = False
    return result



def toString(board):
    for i in range(SIZE):
        st = str(i) + ": "
        for j in range(SIZE):
            lil = "."
            if board[i][j] == True:
                lil = "Q"
            st += lil + " "
        print(st)
    


a = [[False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False]]
addQueen(a, 0)
toString(a)
