def loan_balance(principal, annual_interest_rate, duration,number_of_payments):
    r = (annual_interest_rate/100)/12
    p=number_of_payments
    n=duration*12
    if(annual_interest_rate == 0):
        return principal*(1-(p/n))

    nval = pow((1+r),n)
    pval = pow((1+r),p)
    return principal * (((nval-pval)/(nval-1)))
    

print(loan_balance(1000.0,10.0,5,24))