def absoluteValuesSumMinimization(a):
    if len(a)%2 == 0:
        return a[len(a)//2 - 1]
    else:
        return a[len(a)//2]

#Hint: Get the median
