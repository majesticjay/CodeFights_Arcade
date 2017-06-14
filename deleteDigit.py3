def deleteDigit(n):
    
    arr = list(str(n))
    ans = 0
    for i in range(10):
        t = arr[:]
        c = str(i)
        if c in t:
            t.remove(c)
            n = int(''.join(t))
            if n > ans:
                ans = n
            
    return ans
