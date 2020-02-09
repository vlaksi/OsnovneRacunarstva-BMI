def prosek(niz):
	ret_val = 0
	for x in niz:
		ret_val += x
	ret_val /= len(niz)
	return ret_val

def prosek_1():
	n = int(input("koliko brojeva ima u nizu? "))
	prosek_niza = 0
	for i in range(n):
		broj = float(input("unesi broj: "))
		prosek_niza += broj
	return prosek_niza/n

def prosek_2():
	prosek_niza = 0
	n = 0
	dalje = input("unesi broj: ")
	while dalje != "quit":
		n+=1
		broj = float(dalje)
		prosek_niza += broj
		dalje = input("unesi broj: ")
	return prosek_niza/n

def prosek_3():
	prosek_niza = 0
	n = 0
	while True:
		dalje = input("unesi broj: ")
		if dalje == "q":
			break
		n+=1
		broj = float(dalje)
		prosek_niza += broj
	return prosek_niza/n

def prosek_4():
	prosek_niza = 0
	n = 0
	while True:
		dalje = input("unesi broj: ")
		if dalje == "q":
			break
		broj = float(dalje)
		if broj<0:
			continue
		n+=1
		prosek_niza += broj
	return prosek_niza/n

def fajlovi():
	f = open("prosek.py", "r")
	red = f.readline()
	while red!="":
		print(red)
		red = f.readline()
	f.close()

def fajlovi_1():
	f = open("brojevi.txt", "r")
	red = f.readline()
	suma = 0
	count = 0
	while red!="":
		for broj in red.split(","):
			suma += float(broj)
			count += 1
		red = f.readline()
	f.close()
	return suma/count

def main():
	# print(prosek_4())
	print(fajlovi_1())

if __name__ == '__main__':
	main()