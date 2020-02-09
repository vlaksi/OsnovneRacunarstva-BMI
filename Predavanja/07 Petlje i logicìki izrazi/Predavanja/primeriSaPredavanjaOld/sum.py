# korisnik unosi brojeve sa tasture
# odrediti srednju vrednost unetih brojeva

def sr_vrednost_1():
	n = int(input("koliko brojeva ce biti uneto?"))
	suma = 0
	for i in range(n):
		x = float(input("unesi broj: "))
		suma += x
	srednja_vrednost = suma/n
	return srednja_vrednost

def sr_vrednost_2():
	suma = 0
	n = 1
	dalje = input("da li zelite da unesete jos brojeva? ")
	while dalje != "ne":
		broj = float(input("broj: "))
		suma += broj
		n += 1
		dalje = input("da li zelite da unesete jos brojeva? ")
	return suma/n

def sr_vrednost_3():
	suma = 0
	n = -1
	broj = 1
	while broj != 0:
		broj = float(input("broj: "))
		suma += broj
		n += 1
	return suma/n

def sr_vrednost_4():
	suma = 0
	n = 0
	while True:
		broj = input("broj: ")
		if broj== "q":
			break
		broj = float(broj)
		suma += broj
		n += 1
	return suma/n

# def proba():
# 	while True:
# 		print("!!!")

def sr_vrednost_5():
	suma = 0
	n = 0
	broj = input("broj: ")
	while True:
		broj = float(broj)
		suma += broj
		n += 1
		broj = input("broj: ")
		if broj== "q":
			break
	return suma/n


def main():
	# proba()
	x = sr_vrednost_5()
	print(x)

if __name__ == '__main__':
	main()
