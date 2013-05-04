##Problem 3
balance = 999999
annualInterestRate = 0.18


monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLow = balance / 12.0
monthlyPaymentHigh = (balance * (1 + monthlyInterestRate)**12)/12.0

low_guess = monthlyPaymentLow
high_guess = monthlyPaymentHigh

def finaltally(guess):
    month = 1
    interimBalance = balance
    while month < 13:
        monthlyUnpaidBalance = interimBalance - guess
        interimBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        month += 1
    finalbalance = monthlyUnpaidBalance
    return finalbalance


n = 1

while n < 100:
    guess = (low_guess + high_guess)/2.0
    if finaltally(guess) == 0 or (high_guess-low_guess)/2 < .001:
        print 'Lowest Payment: ' + "{0:.2f}".format(guess)
        break
    n += 1
    if finaltally(guess) > 0:
        low_guess = guess
    else:
        high_guess = guess


    
