#Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. 
inp=int(input("Please enter a positive integer : "))
beginNum=0
for beginNum in range(beginNum,inp+1):
    print(10**beginNum)
    