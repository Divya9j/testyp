def SumEvenNums(a,b):
    sumE=0
    for x in a:
        if(x%2 == 0):
            sumE = sumE + x
    for x in b:
        if(x%2 == 0):
            sumE = sumE + x        
    return sumE