def primer3():
	sum = 0
	counter = 0
	x = input("x: ")
	while x!="":		
		x = eval(x)
		sum += x
		counter += 1
		x = input("x: ")
	srV = sum/counter
	print(srV)

primer3()