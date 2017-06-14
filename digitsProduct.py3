def digitsProduct(product):
    
    if product == 0: return 10
    if product < 10: return product   
    
    s = ''
    
    while True:
        f = bigFactor(product)
        if f == -1: return -1
        if f < 2: break
        product = product//f
        s += str(f)
    
    if len(s) > 0:
        return int(''.join(sorted(s)))
    else:
        return -1
    

def bigFactor(p):
    if p < 10:
        return p
    for n in range(9,1,-1):
        if p%n == 0:
            return n
    return -1
