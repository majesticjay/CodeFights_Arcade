def digitDegree(n):
    
    strn = str(n)
    ans = 0
    
    while len(strn) > 1:
        strn = str(sum(int(c) for c in strn))
        ans += 1
    
    return ans
