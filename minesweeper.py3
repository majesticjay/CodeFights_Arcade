def minesweeper(matrix):
    h,w = len(matrix),len(matrix[0])
    ans = [[0 for x in range(w)] for x in range(h)]
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j]:
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if i == ii and j == jj: continue
                        if ii < 0 or jj < 0: continue
                        if ii >= h or jj >= w: continue
                        ans[ii][jj] += 1
    return ans
