# Import necessary libraries
import numpy as np
import sys
import timeit

from sudokuAlgorithm import *

##############################################'''VALIDATION'''#################################################

''' Check for incorrect rows '''


def checkRow(row, grid, Len):
    temp = grid[row]
    # Remove 0's.
    temp = list(filter(lambda a: a != 0, temp))
    # Check for incorrect values
    # 0 for an incorrect values in row
    if any(i < 0 and i > Len for i in temp):
        return 0
    # Check for repeated values
    # 1 for repeated values in row
    elif len(temp) != len(set(temp)):
        return 1
    else:
        # 2 is returned if the row is valid.
        return 2


''' Check for incorrect columns '''


def checkColumn(col, grid, Len):
    # Extract the column.
    temp = [row[col] for row in grid]
    # Remove 0's.
    temp = list(filter(lambda a: a != 0, temp))
    # Check for incorrect values
    # 0 for an incorrect values in row
    if any(i < 0 and i > Len for i in temp):
        return 0
    # Check for repeated values
    # 1 for repeated values in column
    elif len(temp) != len(set(temp)):
        return 1
    else:
        # 2 is returned if column is correct
        return 2


''' Check for incorrect squares '''


def checkSquares(grid, Len, n):
    for row in range(0, Len, n):
        for col in range(0, Len, n):
            temp = []
            for r in range(row, row+n):
                for c in range(col, col+n):
                    if grid[r][c] != 0:
                        temp.append(grid[r][c])
            # Check for incorrect values
            # 0 for an incorrect values in box
            if any(i < 0 and i > Len for i in temp):
                return 0
            # Check for repeated values
            # 0 for repeated values in box
            elif len(temp) != len(set(temp)):
                return 1
    # 2 is returned if the box is valid
    return 2


''' Check for an incorrect board'''


def checkBoard(grid, Len, n):
    # Check each row and column.
    for i in range(Len):
        checkrow = checkRow(i, grid, Len)
        checkcol = checkColumn(i, grid, Len)
        # If a row or column is incorrect then the board is incorrect.
        if (checkrow < 2 or checkcol < 2):
            return False
    # If the rows and columns are valid then check the subsquares.
    checksquare = checkSquares(grid, Len, n)
    if (checksquare < 2):
        return False
    else:
        return True

################################################"INPUT"########################################################


# To get a  list of command line arguments
# python sudoku_solver.py input1.txt
# In this case sys.argv[1] = 'input1.txt'
fileName = str(sys.argv[1])

# 2D Array
puzzleArray = []

# If puzzle is (9x9)  puzzleSize is 9
# If puzzle is (16x16)  puzzleSize is 16
puzzleSize = 0

# Read the file
inputFile = open(fileName, "r")

for x in inputFile:
    X = x.split()
    puzzleSize = len(X)

    if (puzzleSize == 9 or puzzleSize == 16):
        # Get puzzle values in to an array
        for i in X:
            temp = int(i)
            puzzleArray = np.append(puzzleArray, int(i))
    else:
        print("Invalid Size ! ")

inputFile.close()

###############################################################################################################

# Reshape the puzzle
puzzleArray = puzzleArray.reshape(puzzleSize, puzzleSize)

# List to store lines of puzzle
Line = []
# List to store puzzle
board = []

# Append the puzzle to board list
for line in range(puzzleSize):
    for num in range(puzzleSize):
        Line.append(int(puzzleArray[line][num]))
    board.append(Line)
    Line = []


if (puzzleSize == 9):
    n = 3
elif (puzzleSize == 16):
    n = 4

# Check whether all the conditions are met
isValid = checkBoard(board, puzzleSize, n)

if (isValid == True):
    # start time
    startTime = timeit.default_timer()
    # Start Solving Process
    Board = np.array(board)
    finalSolution = solveSudoku(n, Board)
    # End of the solving process
    # End time
    endTime = timeit.default_timer()
    # Calculate Time
    Time_Taken = endTime - startTime

else:
    finalSolution = None


################################################"OUTPUT"#######################################################

outfileName = fileName.split('.')[0] + '_solution.txt'
outFile = open(outfileName, "w")

if not finalSolution:
    outFile.write("There is no solution!")
else:
    finalSolution = np.array(finalSolution)
    finalSolution = finalSolution.reshape(puzzleSize, puzzleSize)
    for m in range(puzzleSize):
        for n in range(puzzleSize):
            temp = int(finalSolution[m][n])
            line_string = str(temp) + " "
            outFile.write(line_string)
        outFile.write("\n")
    str_Time = "\nTime : " + str(Time_Taken)
    outFile.write(str_Time)

outFile.close()

###############################################################################################################
