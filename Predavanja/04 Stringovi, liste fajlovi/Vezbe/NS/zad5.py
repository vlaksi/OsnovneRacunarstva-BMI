korisnici = open("korisnici.txt","r")
racuni = open("racuni.txt","r")
statistika = open("statistika.txt","w")
lKorisnici = korisnici.readlines()
lRacuni = racuni.readlines()
for i in range(len(lKorisnici)):
	red = lKorisnici[i].split("|")[0]
	racun = 0 
	for r in lRacuni[i].split("|"):
		racun += float(r)
	red += "|" + str(racun)
	prosek = racun / len(lRacuni[i].split("|"))
	red += "|" + str(prosek) + "\n"
	statistika.write(red)

korisnici.close()
racuni.close()
statistika.close()