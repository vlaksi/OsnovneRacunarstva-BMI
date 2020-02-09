def main():
	sum = 0.0
	count = 0
	xStr = input("Unesite broj (<Enter> za kraj) >> ")
	while xStr != "":
		x = eval(xStr)
		sum = sum + x
		count = count + 1
		xStr = input("Unesite broj (<Enter> za kraj) >> ")
	print("\nProsek je", sum / count)

main()