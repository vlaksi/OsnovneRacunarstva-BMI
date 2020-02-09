import math

def median(lista):
	lista.sort()
	if len(lista)%2!=0:
		return lista[int((len(lista)-1)/2)]
	else:
		return (lista[int(len(lista)/2)]+lista[int(len(lista)/2-1)])/2

def stDev(lista, srV):
	v = 0
	for x in lista:
		v+=(srV-x)**2
	v = v/(len(lista)-1)
	stD = math.sqrt(v)
	return stD

def unos():
	xStr = input("Unesite broj (<Enter> za kraj) >> ")
	l = []
	while xStr != "":
		x = eval(xStr)
		l.append(x)
		xStr = input("Unesite broj (<Enter> za kraj) >> ")
	return l

def srVrednost(lista):
	sum = 0.0
	for x in lista:
		sum += x
	retVal = sum/len(lista)
	return retVal

def main():
	lista = unos()
	prosek = srVrednost(lista)
	print("Prosek je", prosek)
	med = median(lista)
	print("median: ",med)
	stD = stDev(lista,prosek)
	print("standardna devijacija: ",stD)
	

main()