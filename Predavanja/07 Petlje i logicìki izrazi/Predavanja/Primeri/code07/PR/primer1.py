def srVrednost():
	n = eval(input("n: "))
	sum = 0
	for i in range(n):
		x = eval(input("x: "))
		sum += x
	srV = sum / n
	print(srV)

srVrednost()
