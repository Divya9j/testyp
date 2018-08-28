def primeNum(x):
    divByOther=False
    if(x==0 or x==1):        
        return False
    else:
        beginNum=2
        while(beginNum < x):
            if(x%beginNum == 0):
                divByOther = True
            beginNum = beginNum+1
    if(divByOther):
        return False
    else:
        return True

print(primeNum(6))