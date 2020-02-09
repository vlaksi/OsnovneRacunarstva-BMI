def main():
	sum = 0.0
	count = 0
	dalje = input("jos brojeva?")
	while dalje!="ne":
		x = eval(input("Unesi broj >> "))
		sum = sum + x
		count += 1
		dalje = input("jos brojeva?")
	print("\nProsek je", sum / count)

main()