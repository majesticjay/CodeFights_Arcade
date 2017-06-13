def alphabeticShift(inputString):
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for c in inputString:
        i = letters.index(c)
        j = i+1
        if j == len(letters): j = 0
        ans += letters[j]
    return ans
