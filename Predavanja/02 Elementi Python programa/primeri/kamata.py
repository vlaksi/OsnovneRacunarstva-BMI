# koliko otplatim za podignuti kredit?
# ulaz: zajam, kamata, broj meseci
# izlaz: vracena suma

# preuzmi zajam sa tastature
# preuzmi kamatu sa tastature
# preuzmi broj meseci sa tastature
# za broj meseci:
#	zajam = zajam + zajam * kamata
# prikazu ukunu vrednost

def kamata():
	# preuzmi zajam sa tastature
	zajam = float(input("zajam: "))	
	# preuzmi kamatu sa tastature
	brojMeseci = int(input("broj meseci: "))	
	# preuzmi broj meseci sa tastature
	kamata = float(input("kamata: "))	
	# za broj meseci:
	for i in range(brojMeseci):
		#zajam = zajam + zajam * kamata
		zajam += zajam * kamata
	# prikazu ukunu vrednost
	print("ukuptno cete vratiti: ", zajam)

kamata()