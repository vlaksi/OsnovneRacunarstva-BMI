import math

def getNumbers():
	lista = []
	xStr = input("Unesite broj (<Enter> za kraj) >> ")
	while xStr != "":
		x = eval(xStr)
		lista.append(x)
		xStr = input("Unesite broj (<Enter> za kraj) >> ")
	return lista

def mean(lista):
	suma = 0
	for x in lista:
		suma += x
	return suma/len(lista)

def median(lista):
	lista.sort()
	retVal = 0
	if len(lista)%2!=0:
		indeks = int((len(lista)-1)/2)
		retVal = lista[indeks]
	else:
		indeks1, indeks2 = int(len(lista)/2 - 1), int(len(lista/2))
		retVal = (lista[indeks1]+lista[indeks2])/2
	return retVal

def stDev(lista):
	m = mean(lista)
	v = 0
	for i in range(len(lista)):
		v += (m-lista[i])**2
	v = v/(len(lista)-1)
	s = math.sqrt(v)
	return s

def main():
	lista = getNumbers()
	m = mean(lista)
	print("mean: ", m)
	mdn = median(lista)
	print("median: ",mdn)
	sd = stDev(lista)
	print("standard deviation: ",sd)

main()