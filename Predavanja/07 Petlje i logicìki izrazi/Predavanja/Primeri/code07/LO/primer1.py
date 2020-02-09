def main():
	n = eval(input("Koliko ima brojeva? "))
	sum = 0.0
	for i in range(n):
		x = eval(input("Unesi broj >> "))
		sum = sum + x
	print("\nProsek je", sum / n)

main()