def listOfMultiples(x):
    beginNum=1
    mylist=[]
    print(beginNum,x)
    while(beginNum <= 5):
        val = x*beginNum
        mylist.append(val)
        print(val)
        beginNum = beginNum + 1
    print(mylist)
    return mylist

print(listOfMultiples(5))
