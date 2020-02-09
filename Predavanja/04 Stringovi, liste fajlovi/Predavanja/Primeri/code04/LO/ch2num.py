tekst = input("unesi tekst: ")
brojevi = ""
for ch in tekst:
	brojevi = brojevi + str(ord(ch)) + " "
brojevi = brojevi[:-1]
print(brojevi)