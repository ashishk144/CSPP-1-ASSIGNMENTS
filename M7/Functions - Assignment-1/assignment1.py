"""Functions | Assignment-1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if aperson
only pays the minimum monthly payment required by the
credit card company each month.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance.
At the end of 12 months, print out the remaining
balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of
Remaining balance: 813.4141998135

So your program only prints out one thing: the remaining balance at the end of
the year in the format:
Remaining balance: 4784.0

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) +
(Monthly interest rate x Monthly unpaid balance)
"""

def paying_debtoffinayear(bal_ance, annual_interestrate, monthly_paymentrate):
    """Defining paying debt function"""
    ba_l = bal_ance
    for _ in range(12):
        pa_y = ba_l*monthly_paymentrate
        u_bal = ba_l - pa_y
        ba_l = u_bal + ((annual_interestrate / 12.0) * u_bal)
    return round(ba_l, 2)

def main():
    """Defining main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: " +str(paying_debtoffinayear(data[0], data[1], data[2])))

if __name__ == "__main__":
    main()
