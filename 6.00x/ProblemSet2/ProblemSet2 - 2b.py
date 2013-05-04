##Problem 2
balance = 4842
annualInterestRate = 0.2



monthlyInterestRate = annualInterestRate/12.0


def finaltally(payment):
    month = 1
	interimBalance = balance
    finalbalance = balance
    minimumPayment = 10
    while month < 13:
        monthlyUnpaidBalance = interimBalance - minimumPayment
        interimBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        month += 1
    finalbalance = monthlyUnpaidBalance
    return finalbalance

    
while finalbalance > 0:
    finaltally(minimumPayment)
    minimumPayment += 10
    
      

print 'Lowest Payment: ' + str(minimumPayment)
