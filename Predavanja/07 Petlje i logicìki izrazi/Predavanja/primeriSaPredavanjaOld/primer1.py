def primer_1():
	f = open("sum.py","r")
	line = f.readline()
	while line != "":
		print(line)
		line = f.readline()
	f.close()

def primer_2():
	f = open("primer1.txt","r")
	line = f.readline()
	sum = 0
	count = 0
	while line != "":
		l_brojvi = line.split(",")
		for x in l_brojvi:
			try:
				sum += float(x)
				count += 1
			except ValueError:
				print("greska!")
		line = f.readline()
	f.close()
	print(sum)
	print(count)

def primer_3():
	scoreA = 0
	scoreB = 0
	# while not((scoreA==15 or scoreB==15) or (scoreA==7 and scoreB==0) or (scoreA==0 and scoreB==15)):
	while (scoreA!=15 and scoreB!=15) and (scoreA!=7 or scoreB!=0) and (scoreA!=0 or scoreB!=15):
		point = input("point: ")
		if point == "a":
			scoreA += 1
		else:
			scoreB += 1
		print("A: ",scoreA,"B: ",scoreB)
	print("A: ",scoreA,"B: ",scoreB)

def primer_4():
	l = []
	broj = input("broj: ")
	while broj!="q":
		l.append(float(broj))
		broj = input("broj: ")
	l.sort()
	print("median: ",l[len(l)//2])
	

primer_4()