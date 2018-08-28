def list2Dsum(dlist):
    totlist=[]    
    for i in range(0,len(dlist)):
        tot = 0
        for j in range(0,len(dlist[i])):
            #print(dlist[i][j])
            tot = tot + dlist[i][j]
        totlist.append(tot)
    return totlist

print(list2Dsum([[1, 2, 5, 4], [1, 2, 3, 4]]))