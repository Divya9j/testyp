def sum2D(dlist):
    tot = 0
    cnt = 0
    for i in range(0,len(dlist)):
        for j in range(0,len(dlist[i])):
            #print(dlist[i][j])
            cnt = cnt + 1
            tot = tot + dlist[i][j];
    return tot/cnt

print(sum2D([[1, 2, 3, 4], [1, 2, 3, 4]]))