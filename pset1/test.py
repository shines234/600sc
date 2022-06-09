balance = 32000
ann_rate = .2
mon_rate = ann_rate/12.0
minpay = 2970
for i in range(12):
    print(i)
    balance = balance*(1+mon_rate)-minpay
print(balance)