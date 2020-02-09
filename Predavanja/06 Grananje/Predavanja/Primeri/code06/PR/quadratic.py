import math
def main():
	try:
		a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
		if b * b - 4 * a * c > 0:
			discRoot = math.sqrt(b * b - 4 * a * c)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)	
			print("\nThe solutions are:", root1, root2)
		elif b * b - 4 * a * c == 0:
			root = -b / (2 * a)
			print("\nThe solution is:", root)
		else:
			print("\nThe equation has no real roots!")	
	except NameError:
		print("The values must be numeric")
main()