import itertools

def stringsRearrangement(inputArray):
    
    p = itertools.permutations(inputArray)
    
    for s in p:
        i = 1
        while i < len(s):
            if goodStrings(s[i],s[i-1]):
                i += 1
                if i == len(s):
                    return True
            else:
                i = len(s)
    
    return False

def goodStrings(s1,s2):
    n = 0
    for c1,c2 in zip(list(s1),list(s2)):
        if c1 != c2:
            n += 1
            if n > 1:
                return False
    return n == 1
