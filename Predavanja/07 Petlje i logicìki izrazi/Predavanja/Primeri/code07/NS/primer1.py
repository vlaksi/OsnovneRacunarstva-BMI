def main():
	n = eval(input("n: "))
	sum = 0
	for i in range(n):
		x = eval(input("unesi broj: "))
		sum += x
	print("prosek: ",sum/n)

main()