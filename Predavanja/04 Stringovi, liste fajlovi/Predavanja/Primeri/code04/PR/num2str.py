num = input("unesi vrednost: ")
numL = num.split()
s = ""
for n in numL:
	s += chr(int(n))
print(s)