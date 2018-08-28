def listExtendSort(list1, list2):    
    sList=[]
    for x in list1:
        sList.append(x)
    for x in list2:        
        sList.append(x)
    i=0
    while i<len(sList) :
        j=0
        while j< (len(sList)-1) :
            if sList[j] < sList[j+1] :
                temp = sList[j]
                sList[j] = sList[j+1]
                sList[j+1] = temp
            j = j+1
                
        i = i+1     
    return sList

print(listExtendSort([1, 0, 2, 3, 4, 10, 7, 8, 2, 9], [100, 2, 3000, -33]))