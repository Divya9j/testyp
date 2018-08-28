def list_of_primes(n):
    primList=[]
    for x in range(2,n):
        divByOther=False
        if(x==0 or x==1):        
            return False
        else:
            beginNum=2
            while(beginNum < x):
                if(x%beginNum == 0):
                    divByOther = True
                beginNum = beginNum+1
        if(not divByOther):
            primList.append(x)
    return primList

print(list_of_primes(6))