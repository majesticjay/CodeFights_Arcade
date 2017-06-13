def boxBlur(image):
    
    hi,wi = len(image),len(image[0])
    
    h,w = hi - 2, wi - 2
    ans = [[0 for x in range(w)] for x in range(h)]
    
    for i in range(hi - 1):
        for j in range(wi - 1):
            sum = 0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    sum += image[ii][jj]
            ans[i-1][j-1] = sum//9
    
    return ans
