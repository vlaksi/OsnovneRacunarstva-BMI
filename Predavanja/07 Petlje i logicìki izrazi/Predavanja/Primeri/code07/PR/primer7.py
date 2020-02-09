def primer7():
	fBrojevi = open("brojevi1.txt", "r")
	sum = 0
	counter = 0
	line=fBrojevi.readline()
	while line!="":
		brojeviL = line.split(",")
		for brojS in brojeviL:			
			try:			
				sum += eval(brojS)
				counter += 1
			except Exception as e:
				print(e)
		line=fBrojevi.readline()
	print(sum/counter)
primer7()