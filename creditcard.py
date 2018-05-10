"""
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the credit card company each month.
"""

"""
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal
"""

#def debtyear(balance, annualInterestRate, monthlyPaymentRate):

for month in range (0, 12, 1):
    monthlyInterestRate = round((annualInterestRate / 12.0), 5)
    #print (monthlyInterestRate)
    minimumMonthlyPayment = monthlyPaymentRate * balance
    #print (minimumMonthlyPayment)
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    #print (monthlyUnpaidBalance)
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    #print(round(balance,2))
    month += 1
print ("Remaining balance: " + str(round(balance,2)))


#print (debtyear(484, 0.2, 0.04))