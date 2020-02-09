def main():
	brojeviF = open("brojevi.txt","r")
	red = brojeviF.readline()
	sum = 0
	n = 0
	while red!="":
		x = eval(red)
		sum += x
		red = brojeviF.readline()		
		n += 1
	brojeviF.close()
	print("prosek: ",sum/n)

main()