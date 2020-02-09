def primer6():
	fBrojevi = open("brojevi.txt", "r")
	sum = 0
	counter = 0
	line=fBrojevi.readline()
	while line!="":
		try:
			sum += eval(line)
			counter += 1
		except SyntaxError as e:
			print(e)
		line=fBrojevi.readline()
	print(sum/counter)
primer6()