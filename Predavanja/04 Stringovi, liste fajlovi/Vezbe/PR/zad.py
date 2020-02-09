def dodajKorisnika():
	ime = raw_input("ime: ")
	lozinka = raw_input("lozinka: ")
	red = ime + "|" +lozinka
	fKorisnici = open("korisnici.txt", "a")
	fKorisnici.write(red+"\n")
	fKorisnici.close()

def prikaziKorisnike():
	fKorisnici = open("korisnici.txt", "r")
	redovi = fKorisnici.readlines()
	for red in redovi:
		if(len(red.split("|"))>1):
			print "ime: "+red.split("|")[0]
			print "lozinka: "+red.strip().split("|")[1]
	fKorisnici.close()

dodajKorisnika()
prikaziKorisnike()