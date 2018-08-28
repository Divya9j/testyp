#Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included)
beginNum=1;
endNum=101;
sum=0;
while beginNum <= endNum :    
    if beginNum%5 == 0 :
        sum = sum + beginNum;
    beginNum = beginNum + 1;
print("Sum is : ", sum);