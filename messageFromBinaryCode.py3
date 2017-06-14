def messageFromBinaryCode(code):
    ans = ''
    i,j = 0,8    
    while j <= len(code):
        s = code[i:j]
        ans += chr(int(s,2))
        i,j = i+8,j+8
    return ans
