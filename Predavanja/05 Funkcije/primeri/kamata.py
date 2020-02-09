def addInterest(balances, rate):
	balances[0] = balances[0] * (1 + rate)

def test():
	amounts = [1000]
	rate = 0.05
	addInterest(amounts, rate)
	print(amounts)

test()