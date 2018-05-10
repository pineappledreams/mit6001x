"""
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
"""

balance = 4773
annualInterestRate = 0.2
monthlyPayment = 10
monthlyInterestRate = round((annualInterestRate / 12.0), 5)


while balance >= 0:
    testBalance = balance

    for month in range (0, 12, 1):
        monthlyUnpaidBalance = testBalance - monthlyPayment
        #print (monthlyUnpaidBalance)
        testBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        #print("month:" + str(month) + "balance:" + str(round(testBalance,2)))
        month += 1

    if testBalance <= 0:
        print ("Lowest payment:" + str(round(monthlyPayment, 2)))
        break
    else:
        monthlyPayment += 10
        #print ("NOW PAYING: " + str(monthlyPayment))
