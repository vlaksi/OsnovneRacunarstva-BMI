import math
def getNumbers():
	l = []
	xStr = input("Unesite broj (<Enter> za kraj) >> ")
	while xStr != "":
		x = eval(xStr)
		l.append(x)
		xStr = input("Unesite broj (<Enter> za kraj) >> ")
	return l

def srVrednost(lista):
	sum = 0.0
	for x in lista:
		sum += x
	return sum / len(lista)

def median(l):
	l.sort()
	x=len(l)
	sri=x//2
	if x%2==0:
		return (l[sri]+l[sri+1])/2
	else: 
		return l[sri]

def stDev(lista):
	s=0
	sredv=srVrednost(lista)
	for i in lista:
		s+=(sredv-i)**2
	p=len(lista)-1
	p=s/p
	p=math.sqrt(p)
	return p

def main():
	lista = getNumbers()
	srV = srVrednost(lista)
	print("srednja vrednost: ", srV)
	m = median(lista)
	print("median: ",m)
	stD = stDev(lista)
	print("standardna devijacija: ",stD)

main()