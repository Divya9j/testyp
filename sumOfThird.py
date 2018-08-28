#Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
beginNum=1;
endNum=1001;
sum=1;
numcount=0;
while beginNum <= endNum :    
    if numcount == 3 :
        #print(beginNum);
        sum = sum + beginNum;
        numcount = 0;
    numcount = numcount +1;
    beginNum = beginNum +1;
print(sum);
