def differentSquares(matrix):
    
    r = len(matrix)
    c = len(matrix[0])
    
    m = []
    
    for i in range(1,r):
        for j in range(1,c):
            t = []
            for ii in [i-1,i]:
                rr = []
                for jj in [j-1,j]:
                    rr.append(matrix[ii][jj]) 
                t.append(rr)
            if t not in m: 
                m.append(t)
    
    return len(m)
