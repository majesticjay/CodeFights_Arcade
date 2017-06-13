def avoidObstacles(inputArray):
    
    inputArray = sorted(inputArray)
    ans = 2
    
    while True:
        
        i = 0
        while i < len(inputArray):
            if inputArray[i] % ans == 0:
                ans += 1
                break
            i += 1
            if i == len(inputArray):
                return ans
