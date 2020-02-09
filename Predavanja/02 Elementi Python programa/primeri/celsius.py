#Analiza
# za zadatu temperaturu u stepenima Celzijusa izracunati i prikazati temperaturu u Farenhajtima

#Specifikacija
# Ulaz: temperatura u stepenima Celzijusa
# Izlaz: temperatura u stepenima Farenhajta
# T(°F) = T(°C) × 9/5 + 32

#Dizajn
#Preuzeti sa tastature vrednost temperature u sepenima Celzijusa
#Prema formuli T(°F) = T(°C) × 9/5 + 32 izracunati temperaturu u stepenima Farenhajta
#Prikazata temperaturu u stepenima Farenhajta

#Implementacija
def c2F():
	#Preuzeti sa tastature vrednost temperature u sepenima Celzijusa
	temperaturaUCelzijusima = float(input("unesite temperaturu u stepenima Celzijusa: "))
	#Prema formuli T(°F) = T(°C) × 9/5 + 32 izracunati temperaturu u stepenima Farenhajta
	temperaturaUFarenhatima = temperaturaUCelzijusima*9/5 + 32
	#Prikazata temperaturu u stepenima Farenhajta
	print("temperatura u stepenima Farenhajta je: ", temperaturaUFarenhatima)
c2F()