def isBeautifulString(inputString):
    
    counts = dict()
    
    letters = list('abcdefghijklmnopqrstuvwxyz')
    
    for c in inputString:
        if c in letters:
            counts[c] = counts.get(c,0) + 1
    
    for c1,c2 in zip(letters,letters[1:]):
        if counts.get(c2,0) > counts.get(c1,0):
            return False
    
    return True
