def maxEven2D(dlist):
    mval = 0
    cnt = 0
    for i in range(0,len(dlist)):
        for j in range(0,len(dlist[i])):
            #print(dlist[i][j])
            if dlist[i][j]%2 == 0 and dlist[i][j] > mval :
                mval = dlist[i][j]            
    if mval != 0:
        return mval
    else:
        return
print(maxEven2D([[1, 1, 3, 1], [1, 1, 3, 1]]))