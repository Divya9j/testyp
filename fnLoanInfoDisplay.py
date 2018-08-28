def monthly_loan_amt(principal, annual_interest_rate, duration):
    r = (annual_interest_rate/100)/12
    n=duration*12
    if(annual_interest_rate == 0):
        return principal/n

    pval = pow((1+r),n)
    return principal * ((r*pval)/(pval-1))

def loan_balance(principal, annual_interest_rate, duration,number_of_payments):
    r = (annual_interest_rate/100)/12
    p=number_of_payments
    n=duration*12
    if(annual_interest_rate == 0):
        return principal*(1-(p/n))

    nval = pow((1+r),n)
    pval = pow((1+r),p)
    return principal * (((nval-pval)/(nval-1)))

principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

beginNum=0
totalPymt=0
monthly_amt = monthly_loan_amt(principal, annual_interest_rate, duration)
print("LOAN AMOUNT: ",int(principal)," INTEREST RATE (PERCENT): ",int(annual_interest_rate))
print("DURATION (YEARS): ",int(duration)," MONTHLY PAYMENT: ",int(monthly_amt))

for beginNum in range(beginNum,duration):
    balance = loan_balance(principal,annual_interest_rate,duration,12*(beginNum+1))
    totalPymt = totalPymt + monthly_amt*12
    print("YEAR: ",beginNum+1, " BALANCE: ",int(balance)," TOTAL PAYMENT ",int(totalPymt))