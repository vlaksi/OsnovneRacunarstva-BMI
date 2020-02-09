# preuzmem vrednost sa tastature
# ako je vrednost "y" ili "Y"
# print Yes
def proba():
	vrednost = input("vrednost: ")
	# if vrednost=="y" or vrednost=="Y":
	if vrednost in ["y","Y"]:
	# if vrednost=="y" or "Y":
		print("Yes")

def main():
	proba()

if __name__ == '__main__':
	main()