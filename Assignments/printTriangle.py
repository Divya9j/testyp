inp=int(input("Enter a postitive integer greater than on equal to 3: "))
if(inp<3):
    print("Enter value greater than or equal to 3")
else:    
    beginNum=1
    while(beginNum <= inp) :
        print("*")
        i=0
        while(i < beginNum+1):
            print "*"
            i = i+1
        beginNum = beginNum+1