# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
totalPaid = 0

for i in range(1, 13):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    totalPaid += minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    print "Month:", i
    print "Minimum monthly payment:", round(minimumMonthlyPayment, 2)
    print "Remaining balance:", round(balance, 2)
    
print "Total paid:", round(totalPaid, 2)
print "Remaining balance:", round(balance, 2)