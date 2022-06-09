from xml.etree.ElementTree import TreeBuilder


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


def p3(balance,ann_rate,minpay):
    mon_rate = ann_rate/12.0
    nmonths = 0
    for i in range(12):
        balance = balance*(1 + mon_rate) - minpay
    return balance

def biset(balance, ann_rate,epsilon):
    mon_rate = ann_rate / 12.0
    low = balance/12.0
    high = (balance*(1+(ann_rate/12))**12)/12.0
    while True:
        
        mid = (low + high)/2.0
        print(low,mid,high)
        if (high - low) < epsilon:
            print(mid)
            break
        # calculate endbal and nmonths at midpay
        # if endbal > 0, search mid to high
        #if endbal < 0, search low to mid
        bal = balance
        for i in range(12):
            bal = bal*(1 + mon_rate) - mid
        if bal < 0:
            high = mid
            mid = (low + high) / 2.0
        else:
            low = mid
            mid = (low + high) / 2.0
            


    







if __name__ == "__main__":
    balance = int(input("balance: " ))
    #rate = float(input("rate: "))
    #minr = float(input("min payment rate: "))
    ann_rate = float(input("annual interest rate: "))
    # minpay = 0
    # endbalance,nmonths = p2(balance,ann_rate,minpay)
    # if nmonths < 13:
    #     print(f"final balance: {endbalance}, months: {nmonths}")
    # else:
    #     while (nmonths > 12):
    #         minpay += 10
    #         endbalance,nmonths = p2(balance,ann_rate,minpay)
    #         print(endbalance,nmonths,minpay)
    #     print(f"final balance: {endbalance}, months: {nmonths}, minpay: {minpay}")
    biset(balance,ann_rate,0.01)