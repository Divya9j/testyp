def fnLCM(x,y):
    beginNum=2
    isFound = False
    while(not isFound):
        if(beginNum%x == 0 and beginNum%y == 0):
            isFound = True
            break
        beginNum = beginNum+1
    return beginNum
print(fnLCM(5,10))