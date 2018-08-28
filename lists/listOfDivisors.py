def divisorsList(x):
    myList=[]    
    for beginNum in range(1,x+1) :
        if(x%beginNum == 0) :
            myList.append(beginNum)
    return myList

print(divisorsList(10))