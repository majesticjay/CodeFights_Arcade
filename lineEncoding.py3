def lineEncoding(s):
    
    p = s[0]
    ans = ''
    count = 1
    
    for c in s[1:]:
        if c != p:
            if count > 1:
                ans += str(count) + p
            else:
                ans += p
            count = 1
        else:
            count += 1
        p = c
        
    if count > 1:
        ans += str(count) + p
    else:
        ans += p
    
    return ans
