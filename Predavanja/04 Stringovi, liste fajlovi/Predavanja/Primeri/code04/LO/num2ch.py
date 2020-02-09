brojevi = input("unesi brojeve: ")
tekst = ""
lista = brojevi.split()
for broj in lista:
	tekst = tekst + chr(int(broj))
print(tekst)