##Problem 2
balance = 3926
annualInterestRate = 0.2


monthlyInterestRate = annualInterestRate/12.0
finalbalance = balance
minimumPayment = 10

while finalbalance > 0:
    month = 1
    interimBalance = balance
    while month < 13:
        monthlyUnpaidBalance = interimBalance - minimumPayment
        interimBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        month += 1
    finalbalance = monthlyUnpaidBalance
    minimumPayment += 10
    


      

print 'Lowest Payment: ' + str(minimumPayment - 10)
