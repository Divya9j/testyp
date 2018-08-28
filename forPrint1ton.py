#Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of all numbers from 1 to n (including both 1 and n)
inp=int(input("Please enter a number : "))
beginNum=1
sum=0
for beginNum in range(beginNum,inp+1):
    sum = sum+beginNum
print(sum);