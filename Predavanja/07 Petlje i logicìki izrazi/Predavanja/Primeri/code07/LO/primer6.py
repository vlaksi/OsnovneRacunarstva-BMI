def main():
	sum = 0.0
	count = 0
	while True:
		xStr = input("Unesi broj >> ")
		if xStr=="":
			break
		x = eval(xStr)
		sum = sum + x
		count = count +1
	print("\nProsek je", sum / count)

main()