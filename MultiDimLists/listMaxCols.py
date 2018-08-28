def listMaxCols(dlist):
    maxlist=[]    
    
    for i in range(0,len(dlist[0])):
        max = 0
        for j in range(0,len(dlist)):
            if dlist[j][i] > max:
                max = dlist[j][i]
        maxlist.append(max)
    return maxlist

print(listMaxCols([[1, 2, 5, 4], [1, 2, 3, 4]]))