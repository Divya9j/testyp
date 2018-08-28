def perfectNum(x):
    beginNum=1
    pnum=0
    while(beginNum<x):
        print("beginNum",beginNum)
        if(x%beginNum ==0):
            print("pNum",pnum)
            pnum = pnum + beginNum
        beginNum=beginNum+1
    print(pnum)
    if(pnum == x):
        return True
    else:
        return False
    
print(perfectNum(6))
