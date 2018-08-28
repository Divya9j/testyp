def find_integer_with_most_divisors(input_list):
    myList=[] 
    cntList=[]   
    i=0
    while i < len(input_list):        
        count=0
        for beginNum in range(1,input_list[i]+1) :
            if(input_list[i]%beginNum == 0) :
                count = count + 1
        cntList.append(count)
        i = i+1
    #print(cntList)

    maxidx = cntList.index(max(cntList))

    return input_list[maxidx]

print(find_integer_with_most_divisors([8, 12, 18, 6]))