def arrayMaxConsecutiveSum(inputArray, k):
    cur_sum = sum(inputArray[:k])
    max_sum = cur_sum
    i = k
    
    for i in range(k, len(inputArray)):
        
        cur_sum = cur_sum - inputArray[i-k] + inputArray[i]
        if cur_sum > max_sum: max_sum = cur_sum
    
    return max_sum
