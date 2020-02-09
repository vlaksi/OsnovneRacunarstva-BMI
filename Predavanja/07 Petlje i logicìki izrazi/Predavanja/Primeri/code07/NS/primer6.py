def main():
	brojeviF = open("brojevi.txt","r")
	red = brojeviF.readline()
	sum = 0
	n = 0
	while red!="":
		brojeviStr = red.split(",")
		for brojStr in brojeviStr:
			try:
				x = eval(brojStr)
				sum += x
				n += 1
			except SyntaxError:
				print("sintaksna greska")
			except NameError:
				print("pogresna vrednost")
		red = brojeviF.readline()		
	brojeviF.close()
	print("prosek: ",sum/n)

main()