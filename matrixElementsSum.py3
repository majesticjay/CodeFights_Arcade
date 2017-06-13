def matrixElementsSum(matrix):
    
    gi = []
    ans = 0
    for a in matrix:
        for i in range(len(a)):
            if i not in gi: ans += a[i]
            if a[i] == 0: gi.append(i)
    
    return ans
