def arrayChange(inputArray):
    
    m = 0
    
    for i in range(1,len(inputArray)):
        
        if inputArray[i] <= inputArray[i-1]:       
            d = inputArray[i-1] - inputArray[i] + 1
            inputArray[i] += d
            m += d
    
    return m
