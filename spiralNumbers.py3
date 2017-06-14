def spiralNumbers(n,m=0,s=1):
    
    if m==0:m=n
    if n==1==m:
        return [[s]]

    #Calculate spiral numbers without first row
    S=spiralNumbers(m-1,n,s+n)
    
    #Create first row and add the transpose of the rest
    return [range(s,s+n)]+zip(*S[::-1])

def my_spiralNumbers(n):
    m = [[0 for x in range(n)] for y in range(n)]
    num = 0
    i,j = 0,0
    r,c = n,n
    rb,cb = 0,0
    while num < n**2:
        if j < c:
            while j < c:
                num += 1 
                m[i][j] = num
                j += 1                               
            j = c-1
        if i < r:
            while i < r:
                i += 1
                if i > r-1: continue
                num += 1
                m[i][j] = num
            rb += 1
            i,j = r-1,c-1
            c -= 1
        if j > cb:
            while j >= cb:
                j -= 1
                if j < cb: continue
                num += 1
                m[i][j] = num
            j = cb
            r -= 1
        if i > rb:
            while i >= rb:
                i -= 1
                if i < rb: continue
                num += 1
                m[i][j] = num
            cb += 1
            i = rb
            j = cb
        
    return m
