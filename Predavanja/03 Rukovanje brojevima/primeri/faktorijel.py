n = eval(input("Unesite prirodan broj: "))
fact = 1.0
for i in range(n,1,-1):
	fact = fact * i
print("Faktorijel od", n, "je", fact)