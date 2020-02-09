brReprezentacija = input("unesi brojcanu reprezentaciju stringa: ")
l = brReprezentacija.split()
rez = ""
for i in l:
	rez += chr(int(i))
print(rez)