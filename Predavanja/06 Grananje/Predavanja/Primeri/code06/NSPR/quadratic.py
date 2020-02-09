import math
print(__name__)
def main():
	try:
		a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
		discrim = b * b - 4 * a * c 
		if discrim > 0:
			discRoot = math.sqrt(discrim)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)
			print("\nThe solutions are:", root1, root2)
		elif discrim == 0:
			discRoot = math.sqrt(discrim)
			root = discRoot / (2 * a)
			print("\nThe solution is:", root)
		else:
			print("\nThere are no real roots")
	except NameError:
		print("\nThe values are not numeric")
	except SyntaxError:
		print("\nThere are syntax error")
main()