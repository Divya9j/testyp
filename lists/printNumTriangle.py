def printNumTriangle(b):    
    pattern=[1,11,111,1111,11111,111111,1111111,11111111,111111111]
    for i in range(1,b+1) :
        #print(pattern[i-1])
        print(i * pattern[i-1])
        #print(sum)
    
printNumTriangle(4)