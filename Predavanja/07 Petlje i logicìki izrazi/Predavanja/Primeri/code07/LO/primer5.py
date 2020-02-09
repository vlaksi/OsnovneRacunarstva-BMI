def main():
	sum = 0.0
	count = 0
	xStr = input("Unesi broj >> ")
	while xStr != "":
		x = eval(xStr)
		sum = sum + x
		count = count +1
		xStr = input("Unesi broj >> ")
	print("\nProsek je", sum / count)

main()