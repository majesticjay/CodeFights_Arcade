def bishopAndPawn(bishop, pawn):
    
    cols = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    
    return abs((cols[bishop[0]] - cols[pawn[0]]) / (int(bishop[1]) - int(pawn[1]))) == 1
