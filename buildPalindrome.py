def buildPalindrome(s):
    t = ''
    while (s+t) != (s+t)[::-1]:
        t = s[len(t)]+t
    return s+t
