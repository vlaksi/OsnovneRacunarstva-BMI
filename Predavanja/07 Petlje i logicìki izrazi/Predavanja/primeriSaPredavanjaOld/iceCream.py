def ice_cream():
	flavour = input("flavour [vanilla]: ")
	if flavour == "":
		flavour = "vanilla"
	print(flavour)


def ice_cream_1():
	flavour = input("flavour [vanilla]: ")
	flavour = flavour or "vanilla"
	print(flavour)

def ice_cream_2():
	flavour = input("flavour [vanilla]: ") or "vanilla"
	print(flavour)

# preuzima aromu sladoleda sa tastature, 
# ako je "" postavlja "vanilla" i ispisuje vrednost
def ice_cream_3():
	print(input("flavour [vanilla]: ") or "vanilla")


def main():
	ice_cream_3()

if __name__ == '__main__':
	main()