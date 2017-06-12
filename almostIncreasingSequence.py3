def almostIncreasingSequence(sequence):
    
    j = firstBadPair(sequence)
    if j == -1: return True
    
    t1 = sequence[:]
    del t1[j]
    
    if firstBadPair(t1) == -1: return True
    
    t2 = sequence[:]
    del t2[j+1]
    
    if firstBadPair(t2) == -1: return True
    
    return False

def firstBadPair(s):
    
    i = 0
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            return i
    return -1
