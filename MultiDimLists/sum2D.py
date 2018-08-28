def sum2D(dlist):
    tot = 0
    for i in range(0,len(dlist)):
        for j in range(0,len(dlist[i])):
            #print(dlist[i][j])
            tot = tot + dlist[i][j];
    return tot

print(sum2D([[1, 2, 3, 4], [1, 2, 3, 4]]))