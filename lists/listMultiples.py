def listOfMultiples(x):
    beginNum=1
    mylist=[]
    while(beginNum <= 5):
        val = x*beginNum
        mylist.append(val)
        beginNum = beginNum + 1
    return mylist

print(listOfMultiples(5))
