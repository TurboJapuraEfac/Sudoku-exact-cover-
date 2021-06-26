# Sudoku-exact-cover-Sudoku is a logic-based number-placement puzzle. The standard Sudoku puzzle consists of
a 9x9 numeric grid that is divided into 9 3x3 sub-grids called “blocks”. The objective of the
puzzle is to fill in the blank cells in a way such that none of the Sudoku rules is violated. The
rules of the standard Sudoku puzzle are as follows:Rules of the Standard Sudoku Puzzle:
● Each cell can only contain a number in the range of 1 to 9 (inclusive).
● For each 3 x 3 block, each number can only occur once.
● Similarly, for each row and column in the puzzle, each number can only occur once.
The blanks can be filled in any order as long as none of the rules above is violated. Once all
the blank spaces are filled in without violating the rules, the puzzle is said to be solved.


You are required to implement an algorithm capable of solving any given standard Sudoku
puzzle as described above. Your implementation must focus on efficiency, and the time
complexity of your solution will be tested (Refer to section 4 below).
Implementation and Requirements
● Your algorithm should be implemented in either Python or C++.
● The algorithm must be able to solve any general solvable standard Sudoku puzzle.
● The input puzzle must be a text file in the root folder of the program and your
program must accept a command-line argument with the name of the input file.
Eg: The command “./sudoku_solver input1.txt” where ‘sudoku_solver’ is the name of
your program and ‘input1.txt’ is the text file containing the input puzzle.
● The input text file must contain the input puzzle in the following format:
○ 9 lines corresponding to the 9 rows
○ Each line contains 9 numbers separated by a single space corresponding to
the 9 columns
○ The blank spaces will be denoted by zeros
○ The text file must not contain any other characters or unnecessary spaces,
tabs etc The solution must also be written to a text file in the root folder of the program. The
output file must be named the same as the input file name with the suffix “_output”
added at the end.
Eg: If “input1.txt” is the input file, the output must be written to a file named
“input1_output.txt”.
● There may be instances where a given puzzle may not have any correct solutions. In
this case, the algorithm must write the string “No Solution” to the output file.


Hexadoku is a variant of the standard Sudoku puzzle where a 16x16 grid is used instead of
the standard 9x9 grid. The 16x16 grid is then divided into 16 4x4 blocks. Instead of using
integers only from 1-9 to fill in the cells, we use the integers from 1- 16 inclusive. The rest of
the rules remain the same as in the standard Sudoku puzzle.
Extend your algorithm in the earlier section to be able to solve Hexadoku puzzles as well.
Your program must be able to detect whether the given input puzzle is a standard 9x9
puzzle or a 16x16 puzzle automatically and adjust accordingly.



The efficiency of your algorithm will be tested. You should aim to have your algorithm solve
9x9 Sudoku puzzles in under 4 seconds on average and 16x16 hexadoku puzzles in under
10 seconds on average.
Hint: See how you could reduce the number of possibilities for each cell and the order in
which you fill in the blank cells.

