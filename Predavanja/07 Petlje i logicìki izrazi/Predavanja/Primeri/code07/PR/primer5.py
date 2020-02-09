def primer5():
	fBrojevi = open("brojevi.txt", "r")
	lines = fBrojevi.readlines()
	sum = 0
	for line in lines:
		sum += eval(line)
	print(sum/len(lines))
primer5()