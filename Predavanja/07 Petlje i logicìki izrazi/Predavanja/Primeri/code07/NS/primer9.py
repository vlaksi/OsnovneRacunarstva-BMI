def main():
	sum = 0
	i = 0
	while True:
		xStr = input("unesi broj: ") 
		if xStr == "":
			break
		x = eval(xStr)
		sum += x
		i += 1 
	print("prosek: ",sum/i)

main()