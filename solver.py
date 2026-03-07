import cli

def isValid(b, row, col, num):

    for x in range(9):
        if b[row][x] == num or b[x][col] == num:
            return False
        
        
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if b[i + startRow][j + startCol] == num:
                return False
    
    return True
            
def solveSudokuRec(b, row, col):
    if row == 8 and col == 9:
        return True
    
    if col == 9:
        row += 1
        col = 0

    if b[row][col] != 0:
        return solveSudokuRec(b, row, col + 1)
    
    for num in range(1,10):

        if isValid(b, row, col, num):
            b[row][col] = num

            if solveSudokuRec(b, row, col + 1):
                return True
            
            b[row][col] = 0

    return False

def solveSudoku(b):
    solveSudokuRec(b, 0, 0)