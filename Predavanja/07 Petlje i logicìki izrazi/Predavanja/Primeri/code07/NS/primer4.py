def main():
	brojeviF = open("brojevi.txt","r")
	lines = brojeviF.readlines()
	brojeviF.close()
	sum = 0
	for red in lines:
		x = eval(red)
		sum += x		
	print("prosek: ",sum/len(lines))

main()