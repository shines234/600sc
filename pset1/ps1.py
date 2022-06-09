def endBal(balance,rate,minrate):
    total = 0
    nmonths = 0
    for i in range(0,12):
        minpay = balance * minrate
        total += minpay
        interest = rate/12.0 * balance
        princ = minpay - interest

        balance -= princ
        nmonths += 1
        print(f"minpay: {minpay} interest: {interest} princ: {princ} balance: {balance}" )

    return balance,nmonths



def p2(balance, ann_rate,minpay):
    mon_rate = ann_rate/12.0
    nmonths = 0
    while (balance > 0):
        balance = balance*(1+mon_rate) - minpay
        nmonths += 1
        if nmonths > 12:
            return balance,13
    return balance,nmonths
    
if __name__ == "__main__":
    balance = int(input("balance: " ))
    #rate = float(input("rate: "))
    #minr = float(input("min payment rate: "))
    ann_rate = float(input("annual interest rate: "))
    minpay = 0
    endbalance,nmonths = p2(balance,ann_rate,minpay)
    if nmonths < 13:
        print(f"final balance: {endbalance}, months: {nmonths}")
    else:
        while (nmonths > 12):
            minpay += 10
            endbalance,nmonths = p2(balance,ann_rate,minpay)
            print(endbalance,nmonths,minpay)
        print(f"final balance: {endbalance}, months: {nmonths}, minpay: {minpay}")
    