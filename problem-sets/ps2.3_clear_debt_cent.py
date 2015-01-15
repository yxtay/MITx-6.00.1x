# balance = 320000
# annualInterestRate = 0.2

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0

low = balance / 12.0
high = balance * (1 + monthlyInterestRate) ** 12 / 12

while True:
    mid = (low + high) / 2
    lowestPayment = mid
    unpaidBalance = balance
    
    for i in range(1, 13):
        monthlyUnpaidBalance = unpaidBalance - lowestPayment
        unpaidBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        
    if round(unpaidBalance, 3) > 0:
        low = mid
    elif round(unpaidBalance, 3) < 0:
        high = mid
    else:
        break
        
print "Lowest Payment:", round(lowestPayment, 2)