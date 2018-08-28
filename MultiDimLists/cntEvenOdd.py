def cntEvenOdd(dlist):
    mlist=[]
    for i in range(0,len(dlist)):        
        mlist.append(max(dlist[i]))
    return(mlist)
print(cntEvenOdd([[1, 1, 3, 1], [1, 1, 3, 1]]))