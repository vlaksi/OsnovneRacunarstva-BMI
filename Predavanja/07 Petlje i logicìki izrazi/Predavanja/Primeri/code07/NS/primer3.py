def main():
	sum = 0
	i = 0
	xStr = input("unesi broj: ") #"3"
	while xStr!="":
		x = eval(xStr)
		sum += x
		i += 1 
		xStr = input("unesi broj: ") #"2",""
	print("prosek: ",sum/i)

main()