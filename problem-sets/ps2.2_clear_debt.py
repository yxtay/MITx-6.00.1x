# balance = 3329
# annualInterestRate = 0.2

balance = 4773
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0

lowestPayment = 10
while True:
    unpaidBalance = balance
    
    for i in range(1, 13):
        monthlyUnpaidBalance = unpaidBalance - lowestPayment
        unpaidBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        
    if unpaidBalance <= 0:
        break
        
    lowestPayment += 10
        
print "Lowest Payment:", lowestPayment