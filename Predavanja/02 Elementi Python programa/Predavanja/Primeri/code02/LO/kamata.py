#ulaz:glavnica
#ulaz:kamata
#ulaz:broj godina
#izlaz:ukupno

#preuzmi glavnicu sa tastature
glavnica = eval(input('unesi glavnicu:'))
#preuzmi kamatu sa tastature
kamata = eval(input('unesi kamatu:'))
#preuzmi broj godina sa tastature
brojGodina = eval(input('unesi broj godina:'))
#za i u (1,broj godina):
for i in range(brojGodina):
	#ukupno=trenutno stanje + trenutno stanje * kamata
	glavnica=glavnica + glavnica*kamata
#ispisi ukupno
print('ukupno stanje je:',glavnica)
