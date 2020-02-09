#izracunavanje zarade u banci
#Ulaz:iznos
#Ulaz:kamata
#Ulaz:broj godina
#Izlaz:ukupni iznos

#unesi iznos sa tastature

iznos=eval(input('unesite iznos'))

#unesi kamatu sa tastature
kamata=eval(input('unesite kamatu'))
#unesi broj godina
godine=eval(input('unesi broj godina'))
#ponovi broj godina puta
for i in range(godine):
	iznos=iznos+iznos*kamata
	#iznos=iznos*(1+kamata)

print('iznos=', iznos)
	#iznos=iznos*kamata

#prikazi iznos
