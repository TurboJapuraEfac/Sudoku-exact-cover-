from itertools import product

##############################################"ALGORITHM X"####################################################

def Select(X, Y, row):
    cols = []
    for j in Y[row]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deSelect(X, Y, row, cols):
    for j in reversed(Y[row]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)

def findSol(X, Y, sol):
    if not X:
        yield list(sol)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            sol.append(r)
            cols = Select(X, Y, r)
            for s in findSol(X, Y, sol):
                yield s
            deSelect(X, Y, r, cols)
            sol.pop()

################################################"EXACT COVER"##################################################

def getExactcover(X, Y):
    X = {j: set() for j in X}
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y


def solvePuzz(n, board):
    # For (9 x 9) , n = 3 and N = 9
    # For (16 x 16) , n = 4 and N = 16
    N = n * n

    X = ([("rc", rc) for rc in product (range(N), range(N))] +
         [("rn", rn) for rn in product (range(N), range(1, N + 1))] +
         [("cn", cn) for cn in product (range(N), range(1, N + 1))] +
         [("bn", bn) for bn in product (range(N), range(1, N + 1))])


    Y = dict()
    for r, c, val in product(range(N), range(N), range(1, N + 1)):
        # Box number
        b = (r // n) * n + (c // n)  
        Y[(r, c, val)] = [
            ("rc", (r, c)),
            ("rn", (r, val)),
            ("cn", (c, val)),
            ("bn", (b, val))]


    # Arrange X using both X and Y
    X, Y = getExactcover(X, Y)

    # Select possible val for each cell in the grid 
    # Remove impossible values from X 
    # Remove impossible constraints
    for r in range (0,N):
        for v in range (0,N):
            if board[r][v] != 0:
                n = board[r][v]
                Select(X, Y, (r, v, n))

    # Solve the grid
    for solution in findSol(X, Y, []):
        for (r, c, val) in solution:
            board[r][c] = val
        yield board


def solveSudoku(n, board):
    ans = list(solvePuzz(n, board))
    return ans



