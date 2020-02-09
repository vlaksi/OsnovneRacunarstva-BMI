def main():
	broj = eval(input ("Unesite broj meseca: "))
	mesec = "JanFebMarAprMajJunJulAvgSepOktNovDec"
	print(mesec[(broj-1)*3:broj*3])
main()