
balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = round((annualInterestRate / 12.0), 7)

lowBound = round((balance / 12), 7)
#print (lowBound)
highBound = round(((balance * (1 + monthlyInterestRate)**12) / 12), 7)
#print (highBound)
middleBound = (lowBound + highBound) / 2
monthlyPayment = middleBound

while balance >= 0:
    testBalance = balance

    for month in range (0, 12, 1):
        monthlyUnpaidBalance = testBalance - monthlyPayment
        #print (monthlyUnpaidBalance)
        testBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        #print("month:" + str(month) + "balance:" + str(round(testBalance,2)))
        month += 1

    testBalance = round(testBalance, 1)

    if testBalance > -0.01 and testBalance < 0.01:
        print ("Lowest payment: " + str(round(monthlyPayment, 2)))
        break
    
    else:
        if testBalance < -0.01:
            highBound = monthlyPayment
            monthlyPayment = (highBound + lowBound) / 2
            #print ("NOW PAYING: " + str(monthlyPayment))
        elif testBalance > 0.01:
            lowBound = monthlyPayment
            monthlyPayment = (lowBound + highBound) / 2
        #print ("NOW PAYING: " + str(monthlyPayment))