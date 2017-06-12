def adjacentElementsProduct(inputArray):
    cur_product = 0
    max_product = -100000
    for i in range(len(inputArray) - 1):
        cur_product = inputArray[i] * inputArray[i+1]
        if cur_product > max_product:
            max_product = cur_product
    return max_product
