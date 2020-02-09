def main():
	fBrojevi = open("brojevi.txt","r")
	sum = 0.0
	count = 0
	line=fBrojevi.readline()
	while line!="":
		print(line)
		try:
			brojevi = line.split(",")
			for broj in brojevi:
				x = eval(broj)
				sum = sum + x
				count = count +1
		except SyntaxError:
			print("pogresna sintaksa u fajlu")
		except NameError:
			print("pogresno uneti podaci u fajlu")
		line=fBrojevi.readline()
	fBrojevi.close()
	print("\nProsek je", sum / count)

main()