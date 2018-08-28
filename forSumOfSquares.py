#Using a for loop, write a program which asks the user to type a positive integer, n, and then prints the sum of the square of all numbers form 1 to n (including both 1 and n).

#For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14

inp=int(input("Please enter positive integer : "))
sum=0
beginNum=1

for beginNum in range(beginNum,inp+1):
    sum = sum + (beginNum**2)
print(sum)