def main():
	n = eval(input("n: "))
	sum = 0
	i = 0
	while i<n:
		x = eval(input("unesi broj: "))
		sum += x
		i += 1 
	print("prosek: ",sum/n)

main()