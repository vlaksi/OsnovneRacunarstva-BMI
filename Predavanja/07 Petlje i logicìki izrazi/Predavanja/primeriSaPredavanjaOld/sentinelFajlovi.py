def citanje_fajla():
	f = open("sum.py","r")
	red = f.readline()
	while red!="":
		print(red)
		red = f.readline()

	f.close()

def main():
	citanje_fajla()

if __name__ == '__main__':
	main()
