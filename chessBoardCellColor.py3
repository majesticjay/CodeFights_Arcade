def chessBoardCellColor(cell1, cell2):   
    
    def cellColor(s):
        letters = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
        p = letters[s[0]] + int(s[1])
        if p%2 == 0:
            return "black"
        else:
            return "white"  
    
    return cellColor(cell1) == cellColor(cell2) 
