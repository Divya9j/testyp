def oddNums(a,b):
    mylist=[]
    while(a<=b):        
        if(a%2 == 1):
            mylist.append(a)
        a = a +1   
    mylist.sort(reverse=True)     
    return mylist

print(oddNums(2,10))