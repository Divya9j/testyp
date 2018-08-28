def listSort(inpList):    
    sList=[]
    for x in inpList:
        sList.append(x)
    i=0
    while i<len(sList) :
        j=0
        while j< (len(sList)-1) :
            if sList[j] > sList[j+1] :
                temp = sList[j]
                sList[j] = sList[j+1]
                sList[j+1] = temp
            j = j+1
                
        i = i+1     
    return sList

print(listSort([10,2,1,8]))