def main():
	a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
	disc = b * b - 4 * a * c 
	if disc<0:
		print("Jednacina nema resenja.")
	else: 
		if disc>0:
			discRoot = math.sqrt(disc)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)
			print("\nThe solutions are:", root1, root2)
		else:#if disc==0:
			discRoot = math.sqrt(disc)
			root = (-b ) / (2 * a)
			print("\nThe solutions are:", root)
main()