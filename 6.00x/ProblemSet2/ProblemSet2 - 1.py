##Problem 1
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0
month = 1
totalPaid = 0.00

while month < 13:
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: '+ "{0:.2f}".format(minimumMonthlyPayment)
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    print 'Remaining balance: ' + "{0:.2f}".format(balance)
    totalPaid +=minimumMonthlyPayment
    month += 1    

print 'Total paid: ' + "{0:.2f}".format(totalPaid)
print 'Remaining balance: ' + "{0:.2f}".format(balance)
