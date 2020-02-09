def main():
	sum = 0.0
	count = 0
	x=1
	while x != 0:
		x = eval(input("Unesi broj >> "))
		sum = sum + x
		count = count +1
	print("\nProsek je", sum / count)

main()