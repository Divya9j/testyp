def list2Dsum(dlist):
    totlist=[]    
    
    for i in range(0,len(dlist[0])):
        tot = 0
        for j in range(0,len(dlist)):
            #print(dlist[j][i])
            tot = tot + dlist[j][i]
        totlist.append(tot)
    return totlist

print(list2Dsum([[1, 2, 5, 4], [1, 2, 3, 4]]))