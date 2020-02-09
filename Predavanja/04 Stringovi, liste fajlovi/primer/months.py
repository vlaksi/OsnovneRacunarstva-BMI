def main():
	months = "JanFebMarAprMayJunJulAvgSepOctNovDec"
	month = int(input("enter the number of the month: "))
	print(months[3*(month-1):3*month])
main()