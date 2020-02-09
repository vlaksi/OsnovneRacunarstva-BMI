def main():
	fKorisnici = open("korisnici1.txt","r")
	fCene = open("cene.txt","r")
	fIzlaz = open("izlaz.txt", "a")
	redoviKorisnici = fKorisnici.readlines()
	redoviCene = fCene.readlines()
	for i in range(len(redoviKorisnici)):
		redIzlaz = ""
		redIzlaz += redoviKorisnici[i].split("|")[0]
		lCene = redoviCene[i].split("|")
		ukupnaCena = 0
		for cena in lCene:
			ukupnaCena += float(cena)
		redIzlaz += "|" + str(ukupnaCena) + "|" + str(ukupnaCena/len(lCene)) + "\n"
		fIzlaz.write(redIzlaz)
	fKorisnici.close()
	fCene.close()
	fIzlaz.close()

main()