def addInterest(balances, rate):
    balances.append(4000)
    for i in range(len(balances)):
        balances[i] = balances[i]*(1+rate)

def test():
    amount = [1000,2000,3000]
    rate = 0.05
    addInterest(amount, rate)
    print(amount)

test()