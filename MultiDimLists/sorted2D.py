def sorted2D(dlist):
    totlist=[]    
    for i in range(0,len(dlist)):               
        dlist[i].sort(reverse=True)
        totlist.append(dlist[i])
    
    return totlist

print(sorted2D([[1, 2, 5, 4], [1, 2, 3, 4]]))