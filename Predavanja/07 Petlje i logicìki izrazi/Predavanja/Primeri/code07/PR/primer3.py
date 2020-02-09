def primer3():
	moreData = "yes"
	sum = 0
	counter = 0
	while moreData[0].lower()=="y":		
		x = eval(input("x: "))
		sum += x
		counter += 1
		moreData = input("more data? ")
	srV = sum/counter
	print(srV)

primer3()