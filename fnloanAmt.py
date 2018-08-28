def monthly_loan_amt(principal, annual_interest_rate, duration):
    r = (annual_interest_rate/100)/12
    n=duration*12
    if(annual_interest_rate == 0):
        return principal/n

    pval = pow((1+r),n)
    return principal * ((r*pval)/(pval-1))
    
print(monthly_loan_amt(1000.0,10,5))