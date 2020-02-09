def unos():
	retVal = []
	xStr = input("Unesite broj (<Enter> za kraj) >> ")
	while xStr != "":
		x = eval(xStr)
		retVal.append(x)
		xStr = input("Unesite broj (<Enter> za kraj) >> ")
	return retVal

def prosek(niz):
	return sum(niz) / len(niz)

def median(niz):
	niz.sort()
	return niz[len(niz)//2]

def stdev(niz):
	m = prosek(niz)
	suma = 0.0
	for x in niz:
		suma += (m-x)**2
	varijansa = suma / (len(niz)-1)
	return varijansa**(1/2)

def main():
	brojevi = unos()
	print("prosek:", prosek(brojevi))
	print("median:", median(brojevi))
	print("standardna devijacija:", stdev(brojevi))



if __name__ == '__main__':
	main()