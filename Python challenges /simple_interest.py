# non compounding interest
def annual_interest_calc(amount, apy):
    amount *= (apy*.01)
    return amount

print(f'${annual_interest_calc(1000, 8)} gained apy not compounding interest')

# compounding interest calc
def annual_compound_interest(amt, apy):
    for _ in range(12):
        monthly_interest_amt = amt*(apy*.01)/12
        amt += monthly_interest_amt

    return amt


print(f'${annual_compound_interest(1000,8)} with compounding interest')