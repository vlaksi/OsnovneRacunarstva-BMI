#Ulaz: Temperatura u C
#Izlaz: Temperatura u F
#F = 9/5C+32

def main():
	#preuzmi temperaturu u C sa tastature
	C = eval(input("unesi temperaturu u C: "))
	#izracunaj temperaturu u F kao F = 9/5C+32
	F = 9/5*C+32
	#ispisi temperaturu u F
	print("temperatura u F je:", F)

main()