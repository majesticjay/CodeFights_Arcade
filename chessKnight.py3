def chessKnight(c):
    x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2

def mychessKnight(cell):

    cols = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    ans = 0
    
    col = cols[cell[0]]
    row = int(cell[1])

    if row+1 <= 8:
        if col+2 <= 8:
            ans += 1
        if col-2 >= 1:
            ans += 1
    if row+2 <= 8:
        if col+1 <= 8:
            ans += 1
        if col-1 >= 1:
            ans += 1
    if row-1 >= 1:
        if col+2 <= 8:
            ans += 1
        if col-2 >= 1:
            ans += 1
    if row-2 >= 1:
        if col+1 <= 8:
            ans += 1
        if col-1 >= 1:
            ans += 1
    
    return ans
