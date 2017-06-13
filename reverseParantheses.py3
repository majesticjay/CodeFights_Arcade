def reverseParentheses(s):
    ob = [] 
    arr = list(s)
    for k,c in enumerate(arr):
        if c == '(': 
            ob.append(k)
        if c == ')': 
            i = ob.pop()
            arr[i:k+1] = reversed(arr[i:k+1])
    return ''.join(c for c in arr if c != '(' and c != ')')
