#factorial
inp = int(input("Please Enter positive integer : "));
beginNum=1;
fact=1;
while beginNum <= inp :
    fact = fact*beginNum; 
    beginNum = beginNum+1;
print(fact);