#konverzija temperate iz stepeni Celzijusa u Farenhajte

#Ulaz: temperatura u stepenima Celzijusa
#Izlaz: temperatura u Farenhajtima
#farenhajti = 9/5 * celzijusi + 32

def main():
	#unesi temperaturu u stepenima Celzijusa
	celzijusi = eval(input("stepeni Celzijusa: "))
	#celzijusi = eval(celzijusi)
	#farenhajti = 9/5 * celzijusi + 32
	farenhajti = 9/5 * celzijusi + 32
	#prikazu temperaturu u farenhajtima
	print(farenhajti)

main()