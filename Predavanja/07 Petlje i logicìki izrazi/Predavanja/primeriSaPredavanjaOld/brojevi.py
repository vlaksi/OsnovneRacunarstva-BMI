# izracunati i prikazati zbir i prosek brojeva iz fajla brojevi.txt

def brojevi_1(ime_fajla):
	f=open(ime_fajla,"r")
	red = f.readline()
	suma=0
	brojac=0
	while red!="":			
		l = red.split(",")
		for x in l:
			try:
				suma += float(x)
				brojac+=1
			except ValueError:
				print("grska u fajlu!")
		red = f.readline()

	f.close()
	return suma, suma/brojac
def main():

	fajl=input("unesite ime fajla: ")
	print(brojevi_1(fajl))

if __name__ == '__main__':
	main()

