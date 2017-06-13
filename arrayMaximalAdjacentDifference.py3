def arrayMaximalAdjacentDifference(inputArray):
    return max(abs(b-a) for a,b in zip(inputArray,inputArray[1:]))
