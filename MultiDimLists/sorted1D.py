def sorted1D(dlist):
    totlist=[]    
    for i in range(0,len(dlist)):       
        for j in range(0,len(dlist[i])) :
            totlist.append(dlist[i][j])
    totlist.sort()
    return totlist

print(sorted1D([[1, 2, 5, 4], [1, 2, 3, 4]]))