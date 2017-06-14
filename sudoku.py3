def sudoku(grid):
    
    for i in range(3):
        for j in range(3):
            cell = list(range(1,10))
            for ii in range(3*i, 3*i + 3):
                for jj in range(3*j, 3*j + 3):
                    n = grid[ii][jj]
                    try:
                        cell.remove(n)
                    except:
                        return False
                    col = [grid[x][jj] for x in range(9)]
                    d = col.count(n) + grid[ii][:].count(n)
                    if d != 2: return False
            if len(cell) > 0: return False
    
    return True

def other_sudoku(grid):

    def r(i):
        return sorted(grid[i]) != list(range(1,10))
    
    def c(i):
        return sorted([grid[x][i] for x in range(9)]) != list(range(1,10))
    
    def g(x,y):
        return sorted([grid[i][j] for i in range(x,x+3) for j in range(y,y+3)]) != list(range(1,10))

    for i in range(9):
        if r(i) or c(i):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if g(i,j):
                return False
    return True
