def knapsackLight(value1, weight1, value2, weight2, maxW):
    
    ans = 0
    
    if value1 < value2:
        
        value1,value2 = value2,value1
        weight1,weight2 = weight2,weight1
    
    if weight1 <= maxW:
        
        ans = value1
        maxW -= weight1
    
    if weight2 <= maxW:
        
        ans += value2
        
    return ans

